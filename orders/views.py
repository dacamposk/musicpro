import random
from django.shortcuts import render, redirect
from carts.models import Cart, CartItem
from carts.views import _cart_id
from app.models import Producto
from .forms import OrderForm
from .models import Order, OrderProduct
from app.models import User
import datetime
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError
from django.utils import timezone
from .models import Payment


def payments(request):
    return render (request,'orders/payments.html')

def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.filter(cart=cart)
    cart_count = cart_items.count()
    print(cart_items)
    if cart_count == 0:
       pass
    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total += (cart_item.producto.precio * cart_item.quantity)
        quantity += cart_item.quantity

    tax = (19 * total) / 100
    grand_total = total + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.region = form.cleaned_data['region']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.is_ordered = False
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            num = random.randint(1,99999999999)

            order_number = current_date + str(num)
            data.order_number = order_number
            data.save()
            grand_total = int(grand_total)
            order = Order.objects.get(user=current_user, is_ordered=False, order_number=order_number)
            
            for cart_item in cart_items:
            
                order_product = OrderProduct()
                order_product.order = order
                order_product.user = current_user
                order_product.producto = cart_item.producto
                order_product.quantity = cart_item.quantity
                order_product.product_price = cart_item.producto.precio
                order_product.ordered = False  
                order_product.save()

        

            context = {
                'orderr': order,
                'total': total,
                'tax': tax,
                'grand_total': grand_total,
                'cart_items': cart_items,
                'order': order_number,
            }
          
            return render(request, 'orders/payments.html', context)

        print('NO POST')

    return redirect('checkout')
def pago(request,total,order):
    order = order
    total = total
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/orders/terminar/'+order

    amount = total
    total= str('{:,.0f}'.format(total).replace(",", "@").replace(".", ",").replace("@", "."))
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        context ={'total':total,"response":response}
        print(amount)

        return render(request, 'orders/pagar.html', context) 
    except TransbankError as e:
        print(e.message)
        print(e.message)
        error =e.message
        context ={'total':total,"error":error,}
        return render(request, 'orders/pagar.html', context)
    


def terminar(request,order):
    token = request.GET.get("token_ws")
    order = Order.objects.get(order_number =order)
    carrito = Cart.objects.filter(user = request.user)
    itemsOrder = OrderProduct.objects.filter(order = order)
  

    try:
        response = Transaction().commit(token) 

        payment = Payment()
        payment.user = request.user  
        payment.order_n = order
        payment.payment_id = token  
        payment.payment_method = "RedCompra"  
        payment.ammount_id = response['amount']  
        payment.status = response['status']   
        payment.created_at = timezone.now()  
        payment.save()

        order.change_ordered_confirm()


        for i in carrito:
             carrito.delete()

        for i in itemsOrder:
            item = Producto.objects.get(SKU= i.producto.SKU )
            item.restar_stock(i.quantity)
            i.change_status_ordered()
            

        

        return render(request, 'orders/terminar.html', {"token": token, "response": response})

    except TransbankError as e:
        error = e.message
        print(e.message)
        print(token)
        return render(request, 'orders/terminar.html', {"error": error})