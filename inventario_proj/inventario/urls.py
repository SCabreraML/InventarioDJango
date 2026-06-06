from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Carreras
    path('carreras/', views.CarreraListView.as_view(), name='carrera_list'),
    path('carreras/nuevo/', views.CarreraCreateView.as_view(), name='carrera_create'),
    path('carreras/editar/<int:pk>/', views.CarreraUpdateView.as_view(), name='carrera_update'),

    # Centros de Costo
    path('centros-costo/', views.CentroCostoListView.as_view(), name='centro_costo_list'),
    path('centros-costo/nuevo/', views.CentroCostoCreateView.as_view(), name='centro_costo_create'),
    path('centros-costo/editar/<int:pk>/', views.CentroCostoUpdateView.as_view(), name='centro_costo_update'),

    # Bodegas
    path('bodegas/', views.BodegaListView.as_view(), name='bodega_list'),
    path('bodegas/nuevo/', views.BodegaCreateView.as_view(), name='bodega_create'),
    path('bodegas/editar/<int:pk>/', views.BodegaUpdateView.as_view(), name='bodega_update'),
]
