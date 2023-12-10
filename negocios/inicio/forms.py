from django import forms
from inicio.models import Equipo, OrdenServicio

class FormEquipo(forms.ModelForm):
    
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'cliente_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Nombre del cliente', 'required': True}
            ),
            'telefono_cliente': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Telefono del cliente', 'required': True}
            ),'tipo_equipo': forms.Select(
                attrs={'class':'form-control','placeholder':'Tipo de equipo', 'required': False}
            ),
            'marca_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Marca', 'required': True}
            ),
            'modelo_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Modelo', 'required': True}
            ),
            'serial_number': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Numero de serie', 'required': False}
            ),
            'accesorios_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Accesorios', 'required': False}
            ),
            'contraseña_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Contraseña del equipo', 'required': False}
            ),
            'sistema_operativo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Sistema Operativo', 'required': True}
            ),
        }
        
class FormServicio(forms.ModelForm):
    
    class Meta:
        model = OrdenServicio
        fields = '__all__'
        widgets = {
            'id_orden': forms.NumberInput(
                attrs={'class':'form-control','placeholder':'Numero de orden', 'required': True}
            ),
            'fecha_orden': forms.DateInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": True}
            ),  
        
            'fecha_entrega':forms.DateInput(
                attrs={'class':'form-control','placeholder':'dd/mm/aaaa',"required": True}
            ),  
            'cotizacion': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Cotizacion', 'required': False}
            ),
            'costo_final': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Costo final', 'required': False}
            ),
            'tipo_servicio': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Tipo de servicio', 'required': True}
            ),'equipo': forms.Select(
                attrs={'class':'form-control','placeholder':'equipo', 'required': False}
            ),
            'indicaciones_adicionales': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Incicaciones', 'required': True}
            ),
            'servicio_realizado': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Servicio realizado', 'required': False}
            ),
            'notas_finales': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Notas Finales', 'required': False}
            ),
            'encargado': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Encargado', 'required': False}
            ),
            'observaciones_notas': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Observaciones', 'required': False}
            ),
            'falla_equipo': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Falla', 'required': True}
            ),
            'partes': forms.TextInput(
                attrs={'class':'form-control','placeholder':'Partes', 'required': False}
            ),
        }
        
