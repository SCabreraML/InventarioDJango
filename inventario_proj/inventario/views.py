from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Carrera, CentroCosto, Bodega, ActivoFijo, CategoriaActivo, Mantenimiento, MovimientoActivo, Insumo, CategoriaInsumo, StockInsumo
from .forms import CarreraForm, CentroCostoForm, BodegaForm, ActivoFijoForm, CategoriaActivoForm, MantenimientoForm, InsumoForm, CategoriaInsumoForm, MovimientoInsumoForm

@login_required
def inicio(request):
    return render(request, 'inicio.html')

# Carrera Views
class CarreraListView(LoginRequiredMixin, ListView):
    model = Carrera
    template_name = 'inventario/carrera_list.html'
    context_object_name = 'carreras'

class CarreraCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('carrera_list')
    success_message = "Carrera creada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Carrera"
        return context

class CarreraUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('carrera_list')
    success_message = "Carrera actualizada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Carrera"
        return context

# Centro Costo Views
class CentroCostoListView(LoginRequiredMixin, ListView):
    model = CentroCosto
    template_name = 'inventario/centro_costo_list.html'
    context_object_name = 'centros'

class CentroCostoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CentroCosto
    form_class = CentroCostoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('centro_costo_list')
    success_message = "Centro de Costo creado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Centro de Costo"
        return context

class CentroCostoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CentroCosto
    form_class = CentroCostoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('centro_costo_list')
    success_message = "Centro de Costo actualizado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Centro de Costo"
        return context

# Bodega Views
class BodegaListView(LoginRequiredMixin, ListView):
    model = Bodega
    template_name = 'inventario/bodega_list.html'
    context_object_name = 'bodegas'

class BodegaCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('bodega_list')
    success_message = "Bodega creada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Bodega"
        return context

class BodegaUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('bodega_list')
    success_message = "Bodega actualizada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Bodega"
        return context

# Activo Fijo Views
class ActivoFijoListView(LoginRequiredMixin, ListView):
    model = ActivoFijo
    template_name = 'inventario/activo_list.html'
    context_object_name = 'activos'

class ActivoFijoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ActivoFijo
    form_class = ActivoFijoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('activo_list')
    success_message = "Activo Fijo registrado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar Activo Fijo"
        return context

class ActivoFijoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ActivoFijo
    form_class = ActivoFijoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('activo_list')
    success_message = "Activo Fijo actualizado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Activo Fijo"
        return context

# Categoria Activo Views
class CategoriaActivoListView(LoginRequiredMixin, ListView):
    model = CategoriaActivo
    template_name = 'inventario/categoria_activo_list.html'
    context_object_name = 'categorias'

class CategoriaActivoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriaActivo
    form_class = CategoriaActivoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('categoria_activo_list')
    success_message = "Categoría creada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Categoría de Activo"
        return context

# Mantenimiento Views
class MantenimientoListView(LoginRequiredMixin, ListView):
    model = Mantenimiento
    template_name = 'inventario/mantenimiento_list.html'
    context_object_name = 'mantenimientos'

class MantenimientoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Mantenimiento
    form_class = MantenimientoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('mantenimiento_list')
    success_message = "Mantenimiento programado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Programar Mantenimiento"
        return context

# Historial de Movimientos
class MovimientoActivoListView(LoginRequiredMixin, ListView):
    model = MovimientoActivo
    template_name = 'inventario/movimiento_activo_list.html'
    context_object_name = 'movimientos'

# Insumo Views
class InsumoListView(LoginRequiredMixin, ListView):
    model = Insumo
    template_name = 'inventario/insumo_list.html'
    context_object_name = 'insumos'

class InsumoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('insumo_list')
    success_message = "Insumo registrado exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Registrar Insumo"
        return context

class CategoriaInsumoListView(LoginRequiredMixin, ListView):
    model = CategoriaInsumo
    template_name = 'inventario/categoria_insumo_list.html'
    context_object_name = 'categorias'

class CategoriaInsumoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoriaInsumo
    form_class = CategoriaInsumoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('categoria_insumo_list')
    success_message = "Categoría de Insumo creada exitosamente."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Categoría de Insumo"
        return context

# Stock Management
class StockInsumoListView(LoginRequiredMixin, ListView):
    model = StockInsumo
    template_name = 'inventario/stock_list.html'
    context_object_name = 'stocks'

@login_required
def registrar_movimiento_insumo(request):
    if request.method == 'POST':
        form = MovimientoInsumoForm(request.POST)
        if form.is_valid():
            insumo = form.cleaned_data['insumo']
            bodega = form.cleaned_data['bodega']
            tipo = form.cleaned_data['tipo']
            cantidad = form.cleaned_data['cantidad']
            lote = form.cleaned_data['lote']
            fecha_caducidad = form.cleaned_data['fecha_caducidad']

            stock, created = StockInsumo.objects.get_or_create(
                insumo=insumo,
                bodega=bodega,
                defaults={'lote': lote, 'fecha_caducidad': fecha_caducidad}
            )

            if tipo == 'ENTRADA':
                stock.cantidad_actual += cantidad
                if lote: stock.lote = lote
                if fecha_caducidad: stock.fecha_caducidad = fecha_caducidad
            else: # SALIDA
                if stock.cantidad_actual < cantidad:
                    messages.error(request, f"Stock insuficiente en {bodega.nombre}. Disponible: {stock.cantidad_actual}")
                    return render(request, 'inventario/movimiento_insumo.html', {'form': form})
                stock.cantidad_actual -= cantidad

            stock.save()
            messages.success(request, f"Movimiento de {tipo} registrado exitosamente.")
            return redirect('stock_list')
    else:
        form = MovimientoInsumoForm()

    return render(request, 'inventario/movimiento_insumo.html', {'form': form})

# Reportes y Alertas
@login_required
def reportes_activos(request):
    carrera_id = request.GET.get('carrera')
    centro_id = request.GET.get('centro')

    activos = ActivoFijo.objects.all()
    if carrera_id:
        activos = activos.filter(carrera_id=carrera_id)
    if centro_id:
        activos = activos.filter(centro_costo_id=centro_id)

    carreras = Carrera.objects.all()
    centros = CentroCosto.objects.all()

    return render(request, 'inventario/reporte_activos.html', {
        'activos': activos,
        'carreras': carreras,
        'centros': centros
    })

@login_required
def dashboard_alertas(request):
    from django.utils import timezone
    from datetime import timedelta

    today = timezone.now().date()
    next_week = today + timedelta(days=7)
    next_month = today + timedelta(days=30)

    # Alertas de mantenimiento (próximos 7 días)
    proximos_mantenimientos = Mantenimiento.objects.filter(
        fecha_programada__lte=next_week,
        estado='Programado'
    )

    # Alertas de stock bajo
    stock_bajo = StockInsumo.objects.filter(cantidad_actual__lte=models.F('cantidad_minima'))

    # Alertas de caducidad (próximos 30 días)
    caducidades = StockInsumo.objects.filter(
        fecha_caducidad__lte=next_month,
        fecha_caducidad__gte=today
    )

    return render(request, 'inventario/dashboard_alertas.html', {
        'mantenimientos': proximos_mantenimientos,
        'stock_bajo': stock_bajo,
        'caducidades': caducidades
    })
