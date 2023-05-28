from django.shortcuts import render, redirect
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



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total +=(cart_item.producto.precio * cart_item.quantity)
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass ##ignora la excepcion

    context = {
        'total': total,
        'quantity ':quantity,
        'cart_items': cart_items
    }

                                
    return render (request, 'app/tienda/cart.html', context)