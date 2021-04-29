from django.urls import path

from . import views  #ServicesApp


urlpatterns = [
    path('', views.services, name="Services"),    
]

