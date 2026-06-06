from django import forms
from .models import Carrera, CentroCosto, Bodega, ActivoFijo, Insumo, CategoriaActivo, CategoriaInsumo

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'codigo', 'coordinador', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'coordinador': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CentroCostoForm(forms.ModelForm):
    class Meta:
        model = CentroCosto
        fields = ['carrera', 'nombre', 'codigo', 'responsable', 'descripcion', 'activo']
        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['nombre', 'tipo_bodega', 'ubicacion', 'descripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_bodega': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
