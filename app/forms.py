import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import Cliente
import datetime
from django.contrib.auth.forms import UserCreationForm




rol= [
    ('',''),
    ('bodeguero','bodeguero'),
    ('vendedor', 'vendedor'),
    ('contador','contador'),
    ]


class NewUserForm(UserCreationForm):
    tipo= forms.CharField(label='Tipo de cuenta ', widget=forms.Select(choices=rol) )

class RegistroClie(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = Cliente
        fields = ['email','contraseña','telefono','ubicacion']
        exclude = ['fechaRegistro']
        widgets = {
           'contraseña': forms.PasswordInput(),
        }
     

class LoginCli(forms.Form):
    email = forms.CharField(label='Email')
    contrasena = forms.CharField(label='Contraseña')

