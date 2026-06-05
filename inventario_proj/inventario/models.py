from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

class Usuario(AbstractUser):
    rol = models.CharField(max_length=10, default='admin')

    @property
    def es_admin(self):
        return self.rol == 'admin' or self.is_superuser

class Categoria(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    producto_surte = models.TextField(blank=True, null=True)
    contacto = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    stock_actual = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    stock_minimo = models.IntegerField(default=5)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Movimiento(models.Model):
    TIPO_CHOICES = (
        ('ENTRADA', 'ENTRADA'),
        ('SALIDA', 'SALIDA'),
    )
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    fecha = models.DateTimeField(auto_now_add=True)
    observacion = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk: # Solo al crear el movimiento
            if self.tipo == 'SALIDA':
                if self.producto.stock_actual < self.cantidad:
                    raise ValueError("No hay suficiente stock para esta salida.")
                self.producto.stock_actual -= self.cantidad
            else: # ENTRADA
                self.producto.stock_actual += self.cantidad
            self.producto.save()
        super().save(*args, **kwargs)