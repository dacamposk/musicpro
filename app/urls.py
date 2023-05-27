from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', RegistroCli, name="RegistroCli"),
    path('store/<slug>', store, name="store"),
    path('store/<slugcat>/<subcatslug>', subCatfilter, name="subCatfilter"),
    path('detalle/<id>', DetalleProducto, name="detalle"),
    path('crud', crud, name="crud"),# INICIO PATH CRUD
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-producto", agreProducto,name="agreProducto"),
    path("nueva-marca", agreMarca,name="agreMarca"),
    path("nuevo-tipoins", agreTipoIns,name="agreTipoIns"),
    path("nuevo-subcategoria", agreSubcat,name="agreSubcat"),
    path('eliminar/<SKU>',delete_Producto, name="delete_Producto"),
    path('nuevo-producto/<SKU>',Mod_Producto, name="Mod_Producto"),
 
]
