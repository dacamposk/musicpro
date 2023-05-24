from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

# Usuarios
class Invitado(models.Model):
    email = models.CharField(max_length=50,primary_key=True)
    telefono = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=30)
    fechaPedido = models.DateTimeField()

class customUserManager (BaseUserManager):
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError('Debe asignar un email valido')
            
        usuario = self.model(
            username = username,
            email = email ,
            password = password
              )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email, username,password ):
        usuario = self.create_user(
            email,
            username = username,
            password = password,
       
            )
       
        usuario.is_staff =True
        usuario.save()
        return usuario
    

    def create_bodeguero(self,email,username,password):
        usuario = self.create_user(
            email,
            username = username,
            password = password,
       
            )
        usuario.groups.add(1) 
        usuario.is_bodeguero =True
        usuario.save()
        return usuario


    
    def create_contador(self,email, username,password):
        usuario = self.create_user(
            email,
            username = username,
            password = password,
       
            )
        usuario.groups.add(2) 
        usuario.is_contador =True
        usuario.save()
        return usuario
    
    
    def create_vendedor(self,email, username,password):
        usuario = self.create_user(
            email,
            username = username,
            password = password,
       
            )
        usuario.groups.add(3) 
        usuario.is_vendedor =True
        usuario.save()
        return usuario

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField('Correo',unique=True)
    username = models.CharField('nombre',max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_bodeguero = models.BooleanField(default=False)
    is_vendedor = models.BooleanField(default=False)
    is_contador = models.BooleanField(default=False)
    objects = customUserManager()
   

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.username
    def has_perm(self, perm, obj = None ):
        return True
    
    def has_module_perms(self, app_label) :
        return True


# Categorias

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria', unique=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.nombreCategoria

class SubCategoria(models.Model):
    nombreSubCategoria = models.CharField(max_length=50, verbose_name='nombre subcategoria')
    descripcion = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'sub category'
        verbose_name_plural = 'sub categories'

    def __str__(self) -> str:
        return self.nombreSubCategoria

class TipoInstrumento(models.Model):
    nombreTipoInstrumento = models.CharField(max_length=50, verbose_name='nombre tipo instrumento', blank=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombreTipoInstrumento


class Marca(models.Model):
    nombreMarca = models.CharField(max_length=50, verbose_name='nombre Marca', unique=True)
    descripcion = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)
    def __str__(self) -> str:
        return self.nombreMarca

class Producto(models.Model):
    SKU = models.IntegerField(primary_key=True, verbose_name='SKU')      
    nombreProducto =  models.CharField(max_length=80 ,verbose_name='nombre')     
    slug = models.CharField(max_length=200, unique = True)
    descripcion = models.TextField(verbose_name='descripcion')
    precio = models.IntegerField(verbose_name='precio')
    imagen=models.ImageField(upload_to='img/productos')
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

