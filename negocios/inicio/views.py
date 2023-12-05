from django.shortcuts import render

# Create your views here.

# Create your views here.


def iniciar_sesion(request):
     
    return render(request, 'login.html')

def registrar(request):
     
    return render(request, 'register.html')

def incio(request):
     
    return render(request, 'index.html')