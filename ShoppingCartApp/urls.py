from django.urls import path

from . import views

urlpatterns = [
    path('', views.go_to_cart, name="cart"),

    path('', views.add_product, name="add"),
    path('', views.delete_product, name="delete"),
    path('cart/increment_product/', views.increment_product, name="increment"),
    path('cart/decrement_product/', views.decrement_product, name="decrement"),
    path('cart/cart_clear/', views.clear_cart, name="clear"),
    path('cart/cart_detail/', views.cart_detail, name="detail"),
]