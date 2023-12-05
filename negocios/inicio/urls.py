from django.urls import path
from inicio import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='IniciarSesion'),
    path('registrar/', views.registrar, name='Registrar'),
    path('principal/', views.incio, name='Inicio'),
    
    
    
]
