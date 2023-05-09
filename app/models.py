from django.db import models

# Create your models here.

class User(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50)
    contraseña = models.CharField(max_length=30)




class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria')
    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    SKU = models.CharField(max_length=6 ,primary_key=True ,verbose_name='SKU')      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')      
    marca = models.CharField(max_length=10,verbose_name='marca')
    precio = models.IntegerField(verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre   


