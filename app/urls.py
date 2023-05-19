from django.urls import path
from .views import home, CrearUsuario, adminView, loginCli, RegistroCli
urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('login', loginCli, name="loginCli"),
    path('registrate', RegistroCli, name="RegistroCli"),
]
