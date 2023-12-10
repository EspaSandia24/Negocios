from django.shortcuts import render, redirect
from inicio.models import Equipo, OrdenServicio
from inicio.forms import FormEquipo, FormServicio
# Create your views here.

# Create your views here.


def iniciar_sesion(request):
     
    return render(request, 'login.html')

def registrar(request):
     
    return render(request, 'register.html')

def incio(request):
     
    return render(request, 'index.html')

def lista_equipos(request):
    
    context={
        'equipo': Equipo.objects.all()
    }
    return render(request, 'equipos/lista_equipos.html',context)

def agregar_equipo(request):
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Equipos')
    else:
        form = FormEquipo()
            
    context = {
        'form' : form
    }     
    return render(request, 'equipos/nuevo_equipo.html', context)

def lista_servicios(request):
    
    context={
        'servicio': OrdenServicio.objects.all()
    }
    return render(request, 'servicios/lista_servicios.html',context)

def agregar_servicio(request):
    if request.method == 'POST':
        form = FormServicio(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Servicios')
    else:
        form = FormServicio()
            
    context = {
        'form' : form
    }     
    return render(request, 'servicios/nuevo_servicio.html', context)