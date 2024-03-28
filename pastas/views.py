from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pastas/index.html')

def about(request):
    return render(request, 'pastas/about.html')

def localiza(request):
    return render(request, 'pastas/localizar.html')

def menu(request):
    return render(request, 'pastas/menu.html')

def contacto(request):
    return render(request, 'pastas/contacto.html')

