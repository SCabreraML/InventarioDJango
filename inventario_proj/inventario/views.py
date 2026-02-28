from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Producto, Transaccion, Usuario

def inicio(request):
    return render(request, 'inventario/inicio.html')

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            error = "Usuario o contraseña incorrectos."
    return render(request, 'inventario/login.html', {'error': error})

@login_required
def producto_list(request):
    productos = Producto.objects.all()

    buscar = request.GET.get('buscar')
    orden = request.GET.get('orden')

    if buscar:
        productos = productos.filter(Q(nombre__icontains=buscar) | Q(codigo__icontains=buscar))

    if orden in ['nombre', 'precio']:
        productos = productos.order_by(orden)

    if request.method == 'POST':
        if request.user.rol not in ['ADMIN', 'CAJERO']:
            return redirect('producto_list')

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')

        if codigo and nombre and cantidad and precio:
            Producto.objects.create(
                codigo=codigo,
                nombre=nombre,
                cantidad=cantidad,
                precio=precio
            )
            return redirect('producto_list')

    contexto = {
        'productos': productos,
        'user': request.user,
    }
    return render(request, 'inventario/productos.html', contexto)


@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'POST':
        # actualizar campos con request.POST
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.cantidad = request.POST.get('cantidad')
        producto.precio = request.POST.get('precio')
        producto.save()
        return redirect('producto_list')

    context = {'producto': producto}
    return render(request, 'inventario/editar_producto.html', context)


@login_required
def eliminar_producto(request, pk):
    if request.user.rol != 'ADMIN':
        return redirect('producto_list')

    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')

    contexto = {
        'producto': producto,
        'tipo': 'producto',
    }
    return render(request, 'inventario/confirmar_eliminar.html', contexto)

@login_required
def transaccion_list(request):
    transacciones = Transaccion.objects.select_related('producto', 'usuario').all()
    productos = Producto.objects.all()

    buscar = request.GET.get('buscar')
    orden = request.GET.get('orden')

    if buscar:
        transacciones = transacciones.filter(
            Q(producto__nombre__icontains=buscar) | 
            Q(usuario__username__icontains=buscar) |
            Q(tipo__icontains=buscar)
        )

    if orden in ['fecha', 'tipo']:
        transacciones = transacciones.order_by(orden)

    if request.method == 'POST':
        if not request.user.puede_crear_transacciones:
            return redirect('transaccion_list')

        producto_id = request.POST.get('producto')
        tipo = request.POST.get('tipo')
        cantidad = int(request.POST.get('cantidad'))

        producto = get_object_or_404(Producto, pk=producto_id)
        try:
            transaccion = Transaccion(producto=producto, usuario=request.user, tipo=tipo, cantidad=cantidad)
            transaccion.save()
            return redirect('transaccion_list')
        except ValueError as e:
            error = str(e)
            context = {'transacciones': transacciones, 'productos': productos, 'error': error}
            return render(request, 'inventario/transacciones.html', context)

    context = {'transacciones': transacciones, 'productos': productos}
    return render(request, 'inventario/transacciones.html', context)

@login_required
def editar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    productos = Producto.objects.all()

    if not request.user.puede_editar_transacciones:
        return redirect('transaccion_list')

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        tipo = request.POST.get('tipo')
        cantidad = int(request.POST.get('cantidad'))

        producto = get_object_or_404(Producto, pk=producto_id)

        # Para editar: revertir efecto antiguo y aplicar el nuevo
        # Muy importante para mantener inventario correcto:
        # Revertir inventario anterior
        if transaccion.tipo == 'VENTA':
            transaccion.producto.cantidad += transaccion.cantidad
        else:
            transaccion.producto.cantidad -= transaccion.cantidad
        transaccion.producto.save()

        # Aplicar nuevos cambios validando stock
        if tipo == 'VENTA' and producto.cantidad < cantidad:
            error = "No hay suficiente inventario para esta venta."
            context = {'transaccion': transaccion, 'productos': productos, 'error': error}
            return render(request, 'inventario/editar_transaccion.html', context)

        transaccion.producto = producto
        transaccion.tipo = tipo
        transaccion.cantidad = cantidad
        transaccion.usuario = request.user
        transaccion.save()
        return redirect('transaccion_list')

    context = {'transaccion': transaccion, 'productos': productos}
    return render(request, 'inventario/editar_transaccion.html', context)

@login_required
def eliminar_transaccion(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    if not request.user.puede_eliminar_transacciones:
        return redirect('transaccion_list')

    if request.method == 'POST':
        # Revertir inventario
        if transaccion.tipo == 'VENTA':
            transaccion.producto.cantidad += transaccion.cantidad
        else:
            transaccion.producto.cantidad -= transaccion.cantidad
        transaccion.producto.save()
        transaccion.delete()
        return redirect('transaccion_list')

    return render(request, 'inventario/confirmar_eliminar.html', {'tipo': 'transacción', 'objeto': transaccion})

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()

    buscar = request.GET.get('buscar')
    orden = request.GET.get('orden')

    if buscar:
        usuarios = usuarios.filter(Q(username__icontains=buscar) | Q(email__icontains=buscar))

    if orden in ['username', 'rol']:
        usuarios = usuarios.order_by(orden)

    if request.method == 'POST' and request.user.es_admin:
        username = request.POST.get('username')
        email = request.POST.get('email')
        rol = request.POST.get('rol')

        if username and email and rol:
            Usuario.objects.create_user(username=username, email=email, rol=rol, password='1234')
            return redirect('usuario_list')

    context = {
        'usuarios': usuarios,
        'user': request.user,  # <-- Agregar esta línea para facilitar acceso en template
    }
    return render(request, 'inventario/usuarios.html', context)


@login_required
def editar_usuario(request, pk):
    usuario_editar = get_object_or_404(Usuario, pk=pk)
    if not usuario_editar.puede_editar(request.user):
        return redirect('usuario_list')

    if request.method == 'POST':
        usuario_editar.username = request.POST.get('username')
        usuario_editar.email = request.POST.get('email')
        usuario_editar.rol = request.POST.get('rol')
        usuario_editar.save()
        return redirect('usuario_list')

    context = {'usuario_editar': usuario_editar}
    return render(request, 'inventario/editar_usuario.html', context)

@login_required
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if not usuario.puede_eliminar(request.user):
        return redirect('usuario_list')

    if request.method == 'POST':
        usuario.delete()
        # Reseteo de PK (solo si usas SQLite, no recomendado para producción)
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='inventario_usuario';")
        return redirect('usuario_list')

    return render(request, 'inventario/confirmar_eliminar.html', {'tipo': 'usuario', 'objeto': usuario})
