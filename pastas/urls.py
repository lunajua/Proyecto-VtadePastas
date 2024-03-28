from django.urls import path 
from pastas import views

app_name = 'pastas'  # Nombre de la aplicacion para poder usarla en el template

urlpatterns = [
    
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contacto, name="contacto"),
    path('localizar/', views.localiza, name="localizar"),
    path('menu/', views.menu, name="menu"),

]