from django.urls import path
from .views import home,CrearUsuario,adminView,loginView
urlpatterns = [
    path('', home, name="home"),
    path('administrador', adminView, name="adminView"),    
    path('registro/', CrearUsuario, name="CrearUsuario"),
  
]
