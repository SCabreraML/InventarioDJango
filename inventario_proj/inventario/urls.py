from django.urls import path
from inventario import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Productos
    path('productos/', views.producto_list, name='producto_list'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    # Transacciones
    path('transacciones/', views.transaccion_list, name='transaccion_list'),
    path('transacciones/editar/<int:pk>/', views.editar_transaccion, name='editar_transaccion'),
    path('transacciones/eliminar/<int:pk>/', views.eliminar_transaccion, name='eliminar_transaccion'),

    # Usuarios
    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
