from django.urls import path
from inicio import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='IniciarSesion'),
    path('registrar/', views.registrar, name='Registrar'),
    path('principal/', views.incio, name='Inicio'),
    path('equipos/', views.lista_equipos, name='Equipos'),
    path('nuevoEquipo/', views.agregar_equipo, name='nuevoEquipo'),
    path('servicios/', views.lista_servicios, name='Servicios'),
    path('nuevoServicio/', views.agregar_servicio, name='nuevoServicio'),
    
    
    
    
    
]
