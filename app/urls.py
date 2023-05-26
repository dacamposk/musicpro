from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', RegistroCli, name="RegistroCli"),
    path('store/<id>', store, name="store"),
    path('store/<id>/<subID>', subCatfilter, name="subCatfilter"),
    path('detalle/<id>', DetalleProducto, name="detalle"),
]
