import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import User

from django.contrib.auth.forms import UserCreationForm




rol= [
    ('',''),
    ('bodeguero','bodeguero'),
    ('vendedor', 'vendedor'),
    ('contador','contador'),
    ]


class NewUserForm(UserCreationForm):
    tipo= forms.CharField(label='Tipo de cuenta ', widget=forms.Select(choices=rol) )



