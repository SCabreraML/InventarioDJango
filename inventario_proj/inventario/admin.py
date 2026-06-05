from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Producto, Movimiento, Categoria, Proveedor

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'rol', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'stock_actual', 'precio']
    search_fields = ['codigo', 'nombre']
    list_filter = ['categoria', 'proveedor']

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'usuario', 'tipo', 'fecha', 'cantidad']
    list_filter = ['tipo', 'fecha']
    date_hierarchy = 'fecha'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'contacto']
