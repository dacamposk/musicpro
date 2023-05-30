from django.urls  import path
from . import views 

urlpatterns = [
    path('',views.cart, name ='cart'),
    path('add_cart/<int:producto_sku>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:producto_sku>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:producto_sku>/', views.remove_cart_item, name='remove_cart_item'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-form/', views.checkout_form, name='checkout_form'),
 


]