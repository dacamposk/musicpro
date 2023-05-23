from django.urls import path
from .views import home, CrearUsuario, adminView, loginCli, RegistroCli, store
from . import views

urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', RegistroCli, name="RegistroCli"),
    path('store', store, name="Store"),
    path('store/<slug:categoria_slug>/', views.store, name="productos_por_categoria"),
    path('store/<slug:categoria_slug>/<slug:subcategoria_slug>/', views.store, name="productos_por_categoria_subcategoria"),
    path('store/<slug:categoria_slug>/<slug:subcategoria_slug>/<slug:tipo_instrumento_slug>/', views.store, name="productos_por_categoria_subcategoria_tipo_instrumento"),


]
