from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Producto, Transaccion
from .forms import UsuarioCreationForm, UsuarioChangeForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ('username', 'email', 'rol', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('rol',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'rol', 'password1', 'password2'),
        }),
    )
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'cantidad', 'precio']
    search_fields = ['codigo', 'nombre']  # Añade búsqueda
    list_filter = ['cantidad']  # Añade filtros

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ['producto', 'usuario', 'tipo', 'fecha', 'cantidad']
    list_filter = ['tipo', 'fecha']  # Añade filtros
    date_hierarchy = 'fecha'  # Navegación por fechas