from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    
    path("encender/", views.encender, name = "encender"),

    path("apagar/", views.apagar, name = "apagar"),
    
    path("desconectar/", views.desconectar, name = "desconectar"),
]