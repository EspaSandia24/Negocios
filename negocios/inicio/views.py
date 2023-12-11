from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from inicio.models import Equipo, OrdenServicio
from inicio.forms import FormEquipo, FormServicio ,UserForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# Create your views here.

class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    
@login_required
def registrar(request):
    usuario_guardado = None  # Inicializar como una instancia vacía
    if request.method == 'POST':
        usuario = request.POST.get('username')
        password = request.POST.get('password')
        email = None
        verificar_password = request.POST.get('password2')

        if password == verificar_password:

             # Verificar si el usuario ya existe en la base de datos
            if User.objects.filter(username=usuario).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
                return render(request, 'register.html')
            
            user = User.objects.create_user(username=usuario, email=email, password=password)
        
            user.save()
            return redirect('Inicio') 
                
    return render(request, 'register.html')

@login_required
def incio(request):
    return render(request, 'index.html')

@login_required
def lista_equipos(request):
    context={
        'equipo': Equipo.objects.all()
    }
    return render(request, 'equipos/lista_equipos.html',context)

@login_required
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

@login_required
def lista_servicios(request):
    
    context={
        'servicio': OrdenServicio.objects.all()
    }
    return render(request, 'servicios/lista_servicios.html',context)

@login_required
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