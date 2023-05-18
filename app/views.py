from django.shortcuts import render, redirect
from .forms import LoginCli,RegistroClie,RegistroEmp
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import User

# Create your views here.

def home (request):
    return render(request, 'app/home.html')


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
    return render(request, 'app/administrador.html')


def loginCli (request):
    data = { 'form' : LoginCli()}
    if request.method == 'POST':
        formulario = LoginCli(data= request.POST)
        if formulario.is_valid():
        
            user = authenticate(    username= formulario.cleaned_data["email"],password= formulario.cleaned_data['contrasena'])
            login(request,user)
            return redirect(to='home')
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


