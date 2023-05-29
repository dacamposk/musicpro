from django.shortcuts import get_object_or_404, render, redirect
from app.models import Producto
from carts.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key 
    if not cart:
        cart= request.session.create()
    return cart
    
def add_cart(request,producto_sku):
    producto = Producto.objects.get(SKU=producto_sku) #obtiene el producto

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #obtiene el carro usando el id del carro en la sesión
    except:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()


    try:
        cart_item = CartItem.objects.get(producto=producto, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            producto = producto,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    return redirect('cart')


def remove_cart(request, producto_sku):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    producto = get_object_or_404(Producto, SKU = producto_sku)
    cart_item = CartItem.objects.get(producto=producto, cart=cart)
    if cart_item.quantity>1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')
    
def remove_cart_item(request, producto_sku):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    producto = get_object_or_404(Producto, SKU = producto_sku)
    cart_item = CartItem.objects.get(producto=producto, cart=cart)
    cart_item.delete()
    return redirect('cart')




def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.producto.precio * cart_item.quantity)
            quantity += cart_item.quantity
        tax = int((19*total) / 100)
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass ##ignora la excepcion

    context = {
        'total': total,
        'quantity ':quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }

                                
    return render (request, 'app/tienda/cart.html', context)



# store/views.py

from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def checkout_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            delivery_option = form.cleaned_data.get('delivery_option')
            form.save()
            if delivery_option == Order.PICKUP:
                return redirect('select_store')  # Redirige a la vista
            else:  
                return redirect('home')  # Redirige a la vista 
    else:
        form = OrderForm()

    return render(request, 'app/tienda/checkout_form.html', {'form': form})

def checkout(request, total=0, quantity=0, cart_items=None):
    tax=0
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.producto.precio * cart_item.quantity)
            quantity += cart_item.quantity
        tax = int((19*total) / 100)
        grand_total = total + tax

    except ObjectDoesNotExist:
        pass ##ignora la excepcion

    context = {
        'total': total,
        'quantity ':quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total
    }

    return render (request, 'app/tienda/checkout.html', context)



