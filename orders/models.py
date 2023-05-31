from django.db import models
from app.models import User, Producto



class Order(models.Model):
    STATUS = (
        ('new', 'Nuevo'),
        ('acepted','aceptado'),
        ('completed','completado'),
        ('cancelelled','cancelado')
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=20 ,primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    order_note = models.CharField(max_length=100)
    order_total = models.IntegerField()
    tax = models.FloatField()
    status = models.CharField(max_length=100, choices=STATUS, default="New")
    ip = models.CharField(blank=True, max_length=20)
    is_ordered = models.BooleanField()
    create_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.email
    
    def full_name(self):
        return f'{self.first_name}{self.last_name}'
    

    def full_address(self):
        return f'{self.address_line_1}{self.address_line_2}'
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_n = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    ammount_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.payment_id
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    product_price= models.IntegerField()
    ordered = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.producto.nombreProducto
    
    