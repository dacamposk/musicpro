from django import forms
from .models import Categoria, Marca, Producto, SubCategoria, TipoInstrumento, User
from django.forms import ModelForm
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
        fields =  ['username','apellido','email','password','telefono']
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
        fields =  ['username','apellido','email','password','telefono']
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

class productoForm (ModelForm):
    class Meta :
        model = Producto
        fields= '__all__'
     


class CategoriaForm (forms.ModelForm):
    class Meta :
        model = Categoria
        fields= '__all__'
    
    

class marcaForm (forms.ModelForm):
    class Meta :
        model = Marca
        fields=  '__all__'
   
        

      #tank = forms.IntegerField(widget=forms.HiddenInput(), initial=123) 
  

       


class subCatForm (forms.ModelForm):
    class Meta :
        model = SubCategoria
        fields= '__all__'


class tipoiForm (forms.ModelForm):
    class Meta :
        model = TipoInstrumento
        fields= '__all__'


