from django.urls import path
from .views import home,CrearUsuario,adminView,loginCli,RegistroCli
urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
    path('Iniciar-Sesion', loginCli, name="loginCli"),
    path('Registrarse', RegistroCli, name="RegistroCli"),
]
