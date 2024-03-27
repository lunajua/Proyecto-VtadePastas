from django.urls import path 
from pastas import views

urlpatterns = [
    
    path('', views.index, name="index")

]