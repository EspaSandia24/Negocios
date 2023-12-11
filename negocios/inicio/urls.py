from django.urls import path
from inicio import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='IniciarSesion'),
    path('registrar/', views.registrar, name='Registrar'),
    path('principal/', views.incio, name='principal'),
    path('equipos/', views.lista_equipos, name='Equipos'),
    path('nuevoEquipo/', views.agregar_equipo, name='nuevoEquipo'),
    path('servicios/', views.lista_servicios, name='Servicios'),
    path('nuevoServicio/', views.agregar_servicio, name='nuevoServicio'),
    path('servicios/eliminarOrden/<int:id_orden>', views.eliminar_orden, name='eliminarOrden'),
    path('servicios/editarOrden/<int:id_orden>', views.editar_orden, name='editarOrden'),
    path('equipos/eliminarEquipo/<int:serial_number>', views.eliminar_equipo, name='eliminarEquipo'),
    path('equipos/editarEquipo/<int:serial_number>', views.editar_equipo, name='editarEquipo'),
    
    
    
    
    
]
