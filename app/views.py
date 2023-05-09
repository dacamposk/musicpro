from django.shortcuts import render, redirect
from .forms import UserForm,NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.

def home (request):
    return render(request, 'app/home.html')


def CrearUsuario(request):
    data = { 'form' : NewUserForm()}
   
    if request.method == 'POST':
        formulario = NewUserForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"],password= formulario.cleaned_data["password1"])
            login (request,user)
            messages.success(request, 'te has registrado correctamente')
            return redirect(to='home')
        data["form"] = formulario
          
    return render(request, 'registration/registro.html', data)

def adminView (request):
    return render(request, 'app/administrador.html')

def loginView (request):
    return render(request, 'app/login.html')


