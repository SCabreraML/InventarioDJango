from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('CAJERO', 'Cajero'),
        ('BODEGA', 'Bodeguero'),
    )
    rol = models.CharField(max_length=10, choices=[('ADMIN', 'Administrador'), ('CAJERO', 'Cajero'), ('BODEGA', 'Bodeguero')])
    

    @property
    def es_admin(self):
        return self.rol == 'ADMIN'

    @property
    def puede_crear_productos(self):
        return self.rol in ['ADMIN', 'BODEGA']

    @property
    def puede_editar_productos(self):
        return self.rol in ['ADMIN', 'BODEGA']

    @property
    def puede_eliminar_productos(self):
        return self.rol == 'ADMIN'

    @property
    def puede_crear_transacciones(self):
        return self.rol in ['ADMIN', 'CAJERO', 'BODEGA']

    @property
    def puede_editar_transacciones(self):
        return self.rol in ['ADMIN', 'CAJERO']

    @property
    def puede_eliminar_transacciones(self):
        return self.rol == 'ADMIN'

    def puede_editar(self, user):
        # Define si el usuario `user` puede editar a este usuario
        return user.es_admin

    def puede_eliminar(self, user):
        # No se puede eliminar a sí mismo y solo admin puede eliminar
        return user.es_admin and self != user

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Transaccion(models.Model):
    TIPOS = (
        ('INGRESO', 'Ingreso'),
        ('VENTA', 'Venta'),
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Validar inventario para ventas
        if self.tipo == 'VENTA':
            if self.producto.cantidad < self.cantidad:
                raise ValueError("No hay suficiente inventario para esta venta.")
            self.producto.cantidad -= self.cantidad
        else:  # INGRESO
            self.producto.cantidad += self.cantidad
        self.producto.save()
        super().save(*args, **kwargs)
