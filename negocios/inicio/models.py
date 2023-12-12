from django.db import models

# Create your models here.

class Equipo (models.Model):
    cliente_equipo = models.TextField(max_length=50, null=False)
    telefono_cliente = models.IntegerField(max_length=10, null=False)
    tipo = [
        ('E','Escritorio-CPU'),
        ('P','Portatil'),
        ('A','AIO'),
        ('I','Impresora'),
        ('M','Multifuncional'),
        ('T','Tablet')  
    ] 
    
    tipo_equipo = models.CharField(max_length=1, choices= tipo, default='P')
    marca_equipo = models.CharField(max_length=30, null=False)
    modelo_equipo = models.CharField(max_length=30, null=False)
    serial_number = models.CharField(max_length=15, null=False, blank=False,unique=True)
    accesorios_equipo = models.TextField(max_length=100)
    contraseña_equipo = models.CharField(max_length=30)
    sistema_operativo = models.TextField(max_length=30, null=False)
    
    def __str__(self):
        return f"{self.cliente_equipo}-{self.serial_number}"
    

class OrdenServicio(models.Model):
    id_orden = models.AutoField(null=False, blank=False, primary_key=True)
    fecha_orden = models.DateField(null=False)
    cotizacion = models.FloatField(max_length=5)
    tipo_servicio = models.CharField(max_length=20, null=False)
    falla_equipo = models.CharField(max_length=200, null=False)
    indicaciones_adicionales = models.CharField(max_length=70, null= False)
    servicio_realizado = models.CharField(max_length=150)
    notas_finales = models.CharField(max_length=150)
    encargado = models.CharField(max_length=50)
    partes = models.CharField(max_length=70)
    fecha_entrega = models.DateField()
    costo_final = models.FloatField(max_length=5.2)
    observaciones_notas = models.CharField(max_length=50)
    equipo = models.ForeignKey(Equipo, null=False, blank=False, on_delete=models.CASCADE)
    
    
