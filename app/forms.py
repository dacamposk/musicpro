from django import forms
from .models import User

rol= [
    ('',''),
    ('bodeguero','bodeguero'),
    ('vendedor', 'vendedor'),
    ('contador','contador'),
    ]

class RegistroEmp(forms.ModelForm):
    tipo = forms.ChoiceField(choices= rol)
    class Meta:
        model = User
        fields =  ['username','email','password']
        widgets = {
            'email': forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'correo electronico',
            }

            ),

              'username': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }

            ),
             'password': forms.PasswordInput()
            
        }
            
class RegistroClie(forms.ModelForm):
    class Meta:
        model = User
        fields =  ['username','email','password']
        widgets = {
            'email': forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'correo electronico',
            }

            ),

              'username': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
            }

            ),
            'password': forms.PasswordInput()
            
        }

  
class LoginCli(forms.Form):
    email = forms.CharField(label='Email')
    contrasena = forms.CharField(label='Contraseña' ,widget= forms.PasswordInput)