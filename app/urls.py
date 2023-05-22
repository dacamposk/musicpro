from django.urls import path
from .views import home, CrearUsuario, adminView, loginCli, RegistroCli, Store
urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', RegistroCli, name="RegistroCli"),
    path('store', Store, name="Store"),
    path('<slug:subcategoria_nombreSubCategoria>/', Store, name="productos_por_categoria"),
]
