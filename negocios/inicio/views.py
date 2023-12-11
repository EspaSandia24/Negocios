from django.shortcuts import render, redirect
from inicio.models import Equipo, OrdenServicio
from inicio.forms import FormEquipo, FormServicio, FormEditarOrden, FormEditarEquipo
# import get_object_or_404()
from django.shortcuts import get_object_or_404
from django.urls import reverse
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

def eliminar_orden(request, id_orden):
    orden = OrdenServicio.objects.get(id_orden = id_orden)
    orden.delete()
    return redirect('Servicios')

def eliminar_equipo(request, serial_number):
    equipo = Equipo.objects.get(serial_number = serial_number)
    equipo.delete()
    return redirect('Equipos')

def editar_orden(request, id_orden):
    orden = OrdenServicio.objects.get(id_orden = id_orden)
    form = FormEditarOrden(instance=orden)

    if request.method == 'POST':
        form = FormEditarOrden(request.POST,  instance=orden)
        if form.is_valid():
            form.save()
            return redirect('Servicios')
            
    context = {
        'form' : form
    }
    return render(request, 'servicios/editar_orden.html', context)

def editar_equipo(request, serial_number):
    equipo = Equipo.objects.get(serial_number = serial_number)
    form = FormEditarEquipo(instance=equipo)

    if request.method == 'POST':
        form = FormEditarEquipo(request.POST,  instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('Equipos')
            
    context = {
        'form' : form
    }
    return render(request, 'equipos/editar_equipo.html', context)