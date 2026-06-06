from django import forms
from .models import Carrera, CentroCosto, Bodega, ActivoFijo, Insumo, CategoriaActivo, CategoriaInsumo, Mantenimiento

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

class CategoriaActivoForm(forms.ModelForm):
    class Meta:
        model = CategoriaActivo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class ActivoFijoForm(forms.ModelForm):
    class Meta:
        model = ActivoFijo
        fields = [
            'carrera', 'centro_costo', 'categoria_activo', 'codigo_inventario',
            'nombre', 'descripcion', 'valor_adquisicion', 'fecha_adquisicion',
            'estado', 'ubicacion_actual', 'activo'
        ]
        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-select'}),
            'centro_costo': forms.Select(attrs={'class': 'form-select'}),
            'categoria_activo': forms.Select(attrs={'class': 'form-select'}),
            'codigo_inventario': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'valor_adquisicion': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_adquisicion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'activo_fijo', 'persona', 'tipo', 'fecha_programada',
            'fecha_realizada', 'descripcion', 'estado'
        ]
        widgets = {
            'activo_fijo': forms.Select(attrs={'class': 'form-select'}),
            'persona': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_programada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_realizada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class CategoriaInsumoForm(forms.ModelForm):
    class Meta:
        model = CategoriaInsumo
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = [
            'categoria_insumo', 'codigo', 'nombre', 'descripcion',
            'unidad_medida', 'es_perecedero', 'activo'
        ]
        widgets = {
            'categoria_insumo': forms.Select(attrs={'class': 'form-select'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'unidad_medida': forms.TextInput(attrs={'class': 'form-control'}),
            'es_perecedero': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class MovimientoInsumoForm(forms.Form):
    TIPOS = (
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    )
    insumo = forms.ModelChoiceField(queryset=Insumo.objects.filter(activo=True), widget=forms.Select(attrs={'class': 'form-select'}))
    bodega = forms.ModelChoiceField(queryset=Bodega.objects.filter(activo=True), widget=forms.Select(attrs={'class': 'form-select'}))
    tipo = forms.ChoiceField(choices=TIPOS, widget=forms.Select(attrs={'class': 'form-select'}))
    cantidad = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    lote = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha_caducidad = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
