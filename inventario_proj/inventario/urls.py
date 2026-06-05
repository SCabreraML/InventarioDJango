from django.urls import path
from inventario import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Productos
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # Movimientos
    path('movimientos/', views.movimiento_list, name='movimiento_list'),

    # Categorias
    path('categorias/', views.categoria_list, name='categoria_list'),

    # Proveedores
    path('proveedores/', views.proveedor_list, name='proveedor_list'),

    # Usuarios
    path('usuarios/', views.usuario_list, name='usuario_list'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
