from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)

urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', asdasdas, name="RegistroCli"),
    path('store/<slug>/', store, name="store"),
    path('store/<slugcat>/<subcatslug>/', subCatfilter, name="subCatfilter"),
    path('detalle/<id>/', DetalleProducto, name="detalle"),
    path('crud', crud, name="crud"),# INICIO PATH CRUD
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-producto", agreProducto,name="agreProducto"),
    path("nueva-marca", agreMarca,name="agreMarca"),
    path("nuevo-tipoins", agreTipoIns,name="agreTipoIns"),
    path("nuevo-subcategoria", agreSubcat,name="agreSubcat"),
    path('eliminar/<SKU>',delete_Producto, name="delete_Producto"),
    path('nuevo-producto/<SKU>',Mod_Producto, name="Mod_Producto"),
    path('vista-user',vistaAdmin, name="vistaAdmin"),
    path('delete-user/<email>',del_user, name="del_user"),
    path('dashboard/',cli_dashboard, name="cli-dashboard"),
    path('api/', include(router.urls)),
]
