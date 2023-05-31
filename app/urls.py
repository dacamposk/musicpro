from django.urls import path, include

from orders.views import terminar
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
    path('registrate', RegistroCli, name="RegistroCli"),
    path('store/<slug>/', store, name="store"),#Filtros store
    path('store/<slugcat>/<subcatslug>/', subCatfilter, name="subCatfilter"),
    path('store/<slugcat>/<subcatslug>/<tiposlug>/', tipoisntruFilter, name="tipoisntruFilter"),
    path('detalle/<id>/', DetalleProducto, name="detalle"),
    path('crud', crud, name="crud"),# INICIO PATH CRUD
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-producto", agreProducto,name="agreProducto"),
    path("nueva-marca", agreMarca,name="agreMarca"),
    path("nuevo-tipoins", agreTipoIns,name="agreTipoIns"),
    path("nuevo-subcategoria", agreSubcat,name="agreSubcat"),
    path('crud/Productos/eliminar/<SKU>/', delete_Producto, name="delete_Producto"),
    path('nuevo-producto/<SKU>',Mod_Producto, name="Mod_Producto"),
    path('vista-user',vistaAdmin, name="vistaAdmin"),
    path('delete-user/<email>',del_user, name="del_user"),
    path('crud/ordenes',vendedorView, name="vendedorView"),
    path('crud/ordenes/<order>/',detalleOrder, name="detalleOrder"),
    path('dashboard/',cli_dashboard, name="cli-dashboard"),
    path('crud/categorias/',categoriasList, name="categoriasList"),
    path('categoria/eliminar/<id>',delete_categoria, name="delete_categoria"),
    path('crud/Marcas/',MarcaList, name="MarcaList"),
    path('crud/marca/eliminar/<str:nombreMarca>/', delete_marca, name="delete_marca"),
    path('crud/Subcategorias/',subcateList, name="subcateList"),
    path('sub-categoria/eliminar/<id>',delete_subcategoria, name="delete_subcategoria"),
    path('crud/Productos/',productosList, name="productosList"),
    path('crud/Tipo-Instrumento/',tipoinsList, name="tipoinsList"),
    path('tipo-inst/eliminar/<id>',delete_tipoinstrumento, name="delete_tipoinstrumento"),
    path('api/', include(router.urls)),
]
