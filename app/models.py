from django.urls import reverse
from typing import Dict, Iterable, Optional, Tuple
from autoslug import AutoSlugField
from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.shortcuts import redirect
from django.utils.text import slugify

# Usuarios
class Invitado(models.Model):
    email = models.CharField(max_length=50,primary_key=True)
    telefono = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=30)
    fechaPedido = models.DateTimeField()


class customUserManager (BaseUserManager):
    def create_user(self,email,username,apellido,password ,telefono):
        if not email:
            raise ValueError('Debe asignar un email valido')
            
        usuario = self.model(
            email = email,
            username = username,
            apellido = apellido,
            password = password,
            telefono = telefono
              )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email, username,apellido,password,telefono):
        usuario = self.create_user(
            email,
            username = username,
            apellido = apellido,
            password = password,
            telefono = telefono
       
            )
   
        usuario.is_staff =True
        usuario.save()
        return usuario
    

    def create_bodeguero(self,email,username,apellido,password,telefono):
        usuario = self.create_user(
            email,
            username = username,
            apellido = apellido,
            password = password,
            telefono = telefono
            )
        usuario.groups.add(1) 
        usuario.is_bodeguero =True
        usuario.save()
        return usuario


    
    def create_contador(self,email, username,apellido,password,telefono):
        usuario = self.create_user(
            email,
            username = username,
            apellido = apellido,
            password = password,
            telefono = telefono
       
            )
        usuario.groups.add(2) 
        usuario.is_contador =True
        usuario.save()
        return usuario
    
    
    def create_vendedor(self,email, username,apellido,password,telefono):
        usuario = self.create_user(
            email,
            username = username,
            apellido = apellido,
            password = password,
            telefono = telefono
            
            )
        usuario.groups.add(3) 
        usuario.is_vendedor =True
        usuario.save()
        return usuario
    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField('Correo',unique=True)
    username = models.CharField('nombre',max_length=255)
    apellido = models.CharField('apellido',max_length=255 ,null=True)
    telefono = models.CharField('telefono',max_length=255 ,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_bodeguero = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_contador = models.BooleanField(default=False)
    objects = customUserManager()
   
   

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username','apellido','telefono']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username
    

    def has_perm(self, perm, obj = None ):
        return True
    
    def has_module_perms(self, app_label) :
        return True




class Region(models.Model):
    nombre = models.CharField(primary_key=True,max_length=80)

class Comuna(models.Model):
    nombre  = models.CharField(primary_key=True,max_length=80)
    region= models.ForeignKey(Region,on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.nombre  


class UserUbicacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=100)
    numero = models.IntegerField()
    comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE)
    region= models.ForeignKey(Region,on_delete=models.CASCADE)
   
   


# Categorias
class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50,primary_key=True, verbose_name='nombre de la categoria', unique=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = AutoSlugField(populate_from='nombreCategoria',null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self) -> str:
        return self.nombreCategoria

class SubCategoria(models.Model):
    nombreSubCategoria = models.CharField(max_length=50,primary_key=True, verbose_name='nombre subcategoria')
    descripcion = models.CharField(max_length=255, blank = True)
    slug = AutoSlugField(populate_from='nombreSubCategoria',null=True) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)   

    class Meta:  
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'

    def __str__(self) -> str:
        return self.nombreSubCategoria

class TipoInstrumento(models.Model):
    nombreTipoInstrumento = models.CharField(max_length=50,primary_key=True ,verbose_name='nombre tipo instrumento', blank=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = AutoSlugField(populate_from='nombreTipoInstrumento',null=True)  
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreTipoInstrumento


class Marca(models.Model):
    nombreMarca = models.CharField(max_length=50,primary_key=True ,verbose_name='nombre Marca', unique=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = AutoSlugField(populate_from='nombreMarca',null=True)
    def __str__(self) -> str:
        return self.nombreMarca

class Producto(models.Model):
    SKU = models.IntegerField(primary_key=True, verbose_name='SKU')      
    nombreProducto =  models.CharField(max_length=80 ,verbose_name='nombre', unique=True)  
    slug = AutoSlugField(populate_from='nombreProducto',null=True)  
    descripcion = models.TextField(verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    imagen=models.ImageField(upload_to='img/productos' , null=True)
    stock = models.IntegerField(verbose_name='stock')
    categoria= models.ForeignKey(Categoria,on_delete=models.CASCADE, )
    subcategoria= models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    tipoinstrumento= models.ForeignKey(TipoInstrumento,on_delete=models.CASCADE, blank=True, null=True)
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
   

    def __str__(self) -> str:
        return self.nombreProducto   
    
    def restar_stock(self,Mcant):
        self.stock = self.stock - Mcant
        self.save()



    
class Sucursal(models.Model):
    nombre  = models.CharField(primary_key=True,max_length=80) 
    calle = models.CharField(max_length=300)
    numero = models.CharField(max_length=10)
    comuna = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)



