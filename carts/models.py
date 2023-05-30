from django.db import models
from app.models import Producto
from app.models import User

# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank = True)
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def _str_(self):
        return self.cart_id
    
    def __str__(self):  
        return str(self.cart_id)  
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.producto.precio * self.quantity

    def __unicode__(self):
        return self.producto
    
    def __str__(self):  
        return str(self.producto)  

from django.db import models

class Order(models.Model):
    PICKUP = 'PU'
    DELIVERY = 'DE'

    DELIVERY_OPTIONS = [
        (PICKUP, 'Retiro en tienda'),
        (DELIVERY, 'Entrega a domicilio'),
    ]

    delivery_option = models.CharField(
        max_length=2,
        choices=DELIVERY_OPTIONS,
        default=PICKUP,
    )

