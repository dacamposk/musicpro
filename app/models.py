from django.db import models
import datetime
# Create your models here.

class Cliente(models.Model):
    email = models.CharField(max_length=50,primary_key=True)
    telefono = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    fechaRegistro = models.DateTimeField(default= datetime.datetime.now())



class Invitado(models.Model):
    email = models.CharField(max_length=50,primary_key=True)
    telefono = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=30)
    fechaPedido = models.DateTimeField()

class SubCategoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreSubCategoria = models.CharField(max_length=50, verbose_name='nombre subcategoria')
    def __str__(self) -> str:
        return self.nombreSubCategoria

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria')
    def __str__(self) -> str:
        return self.nombreCategoria


class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True,verbose_name='marca')
    marca = models.CharField(max_length=50, verbose_name='nombre Marca')
    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    SKU = models.IntegerField(primary_key=True ,verbose_name='SKU')      
    nombre =  models.CharField(max_length=80 ,verbose_name='nombre')      
    valor = models.IntegerField(verbose_name='valor')
    stock = models.IntegerField(verbose_name='stock')
    descripcion = models.TextField(verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    Subcategoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE,blank=True,null=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return self.nombre   






