from django.shortcuts import render, redirect
from .forms import NewUserForm
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
            tipo = formulario.cleaned_data['tipo']
            user = authenticate(username= formulario.cleaned_data["username"],password= formulario.cleaned_data["password1"])
            if tipo == 'bodeguero':        
                user.groups.add(1)   #funcion django que añade el usuario user recien creado al grupo con id 1 en la base de datos
            elif tipo == 'vendedor':
                user.groups.add(2)
            elif tipo == 'contador':
                 user.groups.add(3) 
            else:
                pass #exigir campo    
            messages.success(request, 'te has registrado correctamente')
            return redirect(to='home')
        
        data["form"] = formulario
          
    return render(request, 'registration/registro.html', data)

def adminView (request):
    return render(request, 'app/administrador.html')

def loginView (request):
    return render(request, 'app/login.html')


