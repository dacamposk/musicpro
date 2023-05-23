from django.shortcuts import get_object_or_404, render, redirect
from .forms import LoginCli,RegistroClie,RegistroEmp
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from . models import *
from .models import SubCategoria

# Create your views here.

def home (request):
    productos = Producto.objects.all().filter(is_available=True)

    context = {
        'productos': productos,
    }
    return render(request, 'app/home.html', context)


def CrearUsuario(request):
    data = { 'form' : RegistroEmp()}
    if request.method == 'POST':
        formulario = RegistroEmp(data= request.POST)
        if formulario.is_valid():
            tipo = formulario.cleaned_data["tipo"]
            email = formulario.cleaned_data["email"]
            username= formulario.cleaned_data["username"]
            password = formulario.cleaned_data["password"]
            print(tipo,email,username,password)
            # funcion que llama al manager custom de user para crear un usuario bodeguero, revisar models customuser
            if tipo == 'bodeguero' :
                User.objects.create_bodeguero(email,username,password) 
            elif tipo == 'vendedor':
                 User.objects.create_vendedor(email,username,password) 
            elif tipo == 'contador':
                User.objects.create_contador(email,username,password) 
            else:
                pass
            messages.success(request, 'te has registrado correctamente')
            return redirect(to='home')
        
        data["form"] = formulario
          
    return render(request, 'registration/registro.html', data)

def adminView (request):
    return render(request, 'app/vistaAdmin.html')


def loginCli (request):
    data = { 'form' : LoginCli()}
    if request.method == 'POST':
        formulario = LoginCli(data= request.POST)
        if formulario.is_valid():
            user = authenticate(username= formulario.cleaned_data["email"],password= formulario.cleaned_data['contrasena'])
            if user is not None:
                login(request,user)
                return redirect(to='home')
            else :
                pass #Falta ponner mensaje de alerta o similar
        data["form"] = formulario
        
    return render(request, 'app/loguinCli.html',data)

def RegistroCli (request):
    
    if request.method == 'GET':
       data = { 'form' : RegistroClie()}
       return render(request, 'registration/registroCli.html',data)
    
    else:
        if request.method == 'POST':
            formulario = RegistroClie(data= request.POST)
            if formulario.is_valid():
                email = formulario.cleaned_data["email"]
                username= formulario.cleaned_data["username"]
                password = formulario.cleaned_data["password"]
                User.objects.create_user(email,username,password) 
                return redirect(to='home')
            data["form"] = formulario
    return render(request, 'registration/registroCli.html',data)

def store (request, categoria_slug=None, subcategoria_slug=None, tipo_instrumento_slug=None):
    categorias = None
    productos = None
    subcategoria = None
    tipo_instrumento = None

    if categoria_slug != None:
        categorias = get_object_or_404(Categoria, slug=categoria_slug)
        if subcategoria_slug is not None:
            subcategoria = get_object_or_404(SubCategoria, slug=subcategoria_slug)
            if tipo_instrumento_slug is not None:
                tipo_instrumento = get_object_or_404(TipoInstrumento, slug=tipo_instrumento_slug)
                productos = Producto.objects.filter(categoria=categorias, subcategoria=subcategoria, tipoinstrumento=tipo_instrumento, is_available=True)
            else:
                productos = Producto.objects.filter(categoria=categorias, subcategoria=subcategoria, is_available=True)
        else:
            productos = Producto.objects.filter(categoria=categorias, is_available=True)
        producto_count = productos.count()
    else:
        productos = Producto.objects.all().filter(is_available=True)
        producto_count = productos.count()

    context = {
        'productos': productos,
        'producto_count': producto_count,
    }
    return render(request, 'app/tienda/store.html', context)