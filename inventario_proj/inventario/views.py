from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Carrera, CentroCosto, Bodega
from .forms import CarreraForm, CentroCostoForm, BodegaForm

@login_required
def inicio(request):
    return render(request, 'inicio.html')

# Carrera Views
class CarreraListView(LoginRequiredMixin, ListView):
    model = Carrera
    template_name = 'inventario/carrera_list.html'
    context_object_name = 'carreras'

class CarreraCreateView(LoginRequiredMixin, CreateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('carrera_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Carrera"
        return context

class CarreraUpdateView(LoginRequiredMixin, UpdateView):
    model = Carrera
    form_class = CarreraForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('carrera_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Carrera"
        return context

# Centro Costo Views
class CentroCostoListView(LoginRequiredMixin, ListView):
    model = CentroCosto
    template_name = 'inventario/centro_costo_list.html'
    context_object_name = 'centros'

class CentroCostoCreateView(LoginRequiredMixin, CreateView):
    model = CentroCosto
    form_class = CentroCostoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('centro_costo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Centro de Costo"
        return context

class CentroCostoUpdateView(LoginRequiredMixin, UpdateView):
    model = CentroCosto
    form_class = CentroCostoForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('centro_costo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Centro de Costo"
        return context

# Bodega Views
class BodegaListView(LoginRequiredMixin, ListView):
    model = Bodega
    template_name = 'inventario/bodega_list.html'
    context_object_name = 'bodegas'

class BodegaCreateView(LoginRequiredMixin, CreateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('bodega_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear Bodega"
        return context

class BodegaUpdateView(LoginRequiredMixin, UpdateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/form.html'
    success_url = reverse_lazy('bodega_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar Bodega"
        return context
