from django.urls import path, include
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('pago/<int:total>/', views.pago, name='pago'),
    path("terminar/", views.terminar,name="terminar"),
    ]
