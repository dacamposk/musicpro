from django.db import models

# Create your models here.

class User(models.Model):
    usuario = models.CharField(primary_key=True, max_length=50)
    contraseña = models.CharField(max_length=30)