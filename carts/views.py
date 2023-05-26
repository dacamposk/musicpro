from django.shortcuts import render
from app.models import Producto
from carts.models import Cart, CartItem

# Create your views here.

def _cart_id(request):
    cart = request.sessions.sessions_key 
    if not cart:
        cart= request.session.create()
    return cart
    
def add_cart(request,producto_id):
    producto = Producto.objetcs.get(id=producto_id) #obtiene el producto

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

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            producto = producto,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    
    return redirect('cart')



def cart(request):
    return render (request, 'app/tienda/cart.html')