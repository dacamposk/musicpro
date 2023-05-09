import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import User

from django.contrib.auth.forms import UserCreationForm



class UserForm (ModelForm):
    class Meta :
        model = User
        fields= ['usuario','contraseña',]


class NewUserForm(UserCreationForm):
    pass