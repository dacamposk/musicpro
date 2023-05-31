from django.urls import path, include
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('pago/<int:total>/<order>', views.pago, name='pago'),
    path("terminar/<order>", views.terminar,name="terminar"),
    ]
