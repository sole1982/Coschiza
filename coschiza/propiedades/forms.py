from django import forms
from .models import Propiedad, ImagenPropiedad

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'  # Usamos todos los campos del modelo
        widgets = {
                        'tipo_propiedad': forms.Select(attrs={'class': 'form-select'}),
            'estado_publicacion': forms.Select(attrs={'class': 'form-select'}),

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'piso': forms.TextInput(attrs={'class': 'form-control'}),
            'entre_calles': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'cochera_fija': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'orientacion': forms.TextInput(attrs={'class': 'form-control'}),
            'luminosidad': forms.TextInput(attrs={'class': 'form-control'}),
            'amueblado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'balcon_terraza': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ubicacion_en_planta': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}, choices=[('Muy bueno', 'Muy bueno'), ('Bueno', 'Bueno'), ('Regular', 'Regular')]),
            'agua_caliente': forms.TextInput(attrs={'class': 'form-control'}),
            'superficie_cubierta': forms.NumberInput(attrs={'class': 'form-control'}),
            'superficie_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria_edificio': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_pisos': forms.NumberInput(attrs={'class': 'form-control'}),
            'apto_profesional': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gas_natural': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'desagues_cloacales': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pavimento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'agua_corriente': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'expensas': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes_expensas': forms.TextInput(attrs={'class': 'form-control'}),
            'palier': forms.TextInput(attrs={'class': 'form-control'}),
            'toilette_recepcion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cantidad_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'dormitorio': forms.TextInput(attrs={'class': 'form-control'}),
            'cocina': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
from django import forms

from django import forms

class ImagenPropiedadForm(forms.Form):
    imagenes = forms.FileField(widget=forms.FileInput(), required=False)

class TasacionForm(forms.Form):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
