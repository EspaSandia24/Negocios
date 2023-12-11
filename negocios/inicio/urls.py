from django.urls import path
from inicio import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.LoginView.as_view(), name='IniciarSesion'),
    path('registrar/', views.registrar, name='Registrar'),
    path('principal/', views.incio, name='Inicio'),
    path('equipos/', views.lista_equipos, name='Equipos'),
    path('nuevoEquipo/', views.agregar_equipo, name='nuevoEquipo'),
    path('servicios/', views.lista_servicios, name='Servicios'),
    path('nuevoServicio/', views.agregar_servicio, name='nuevoServicio'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    
    
    
    
    
]
