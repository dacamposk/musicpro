from django.shortcuts import render, redirect
from carts.models import CartItem
from .forms import OrderForm
from .models import Order
from app.models import User
import datetime

def place_order(request, total =0,quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()

    if cart_count == 0:
       print(cart_count,'fallo',cart_items)
    print(cart_count,'funciono',cart_items)
    grand_total = 0
    tax = 0

    for cart_item in cart_items:
        total+=(cart_item.producto.precio * cart_item.quantity)
        quantity += cart_item.quantity
    
    tax =(19*total)/100
    grand_total = total + tax

    if request.method =='POST':
        form = OrderForm(request.POST)
        print(form, 'fuera if')
        if form.is_valid():
            print(form)
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data['first_name']
            data.last_name= form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_line_1 = form.cleaned_data[ 'address_line_1']
            data.address_line_2=form.cleaned_data[ 'address_line_2']
            data.region = form.cleaned_data['region']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.is_ordered = True
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            yr = int(datetime.date.today().strftime('%Y'))
            mt = int(datetime.date.today().strftime('%m'))
            dt = int(datetime.date.today().strftime('%d'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")

            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('home')
    else:
        return redirect('checkout')
