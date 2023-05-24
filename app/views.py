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
    categorias = Categoria.objects.all()
    SubCat = SubCategoria.objects.all()

    context = {'productos': productos,'categorias':categorias}
    return render(request, 'app/base.html', context)


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

def store (request, id):

    tipo = None
    subcat = SubCategoria.objects.filter(categoria=id)
    productos = Producto.objects.filter(categoria=id)
    categorias = Categoria.objects.all()

    context = {
        'tipo':tipo,
        'subCat':subcat,
        'categorias':categorias,
        'productos': productos,
    }
    return render(request, 'app/tienda/store.html', context)

def subCatfilter (request,id,subID):

    categorias = Categoria.objects.all()
    subcat = SubCategoria.objects.filter(categoria_id=id)
    productos = Producto.objects.filter(subcategoria=subID)
    tipo = TipoInstrumento.objects.filter(subcategoria= subID) 
    print(id)

    context = {
        'tipo':tipo,
        'subCat':subcat,
        'categorias':categorias,
        'productos': productos,
    }
    return render(request, 'app/tienda/store.html', context)

def detalle(request,  id):
       datos = Producto.objects.filter(SKU=id)
       producto = {'producto':datos}
       
       return render(request, 'app/tienda/detalle.html', producto)
