from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Producto, Movimiento, Usuario, Categoria, Proveedor
from django.db import IntegrityError

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

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def producto_list(request):
    productos = Producto.objects.all()

    buscar = request.GET.get('buscar')
    if buscar:
        productos = productos.filter(Q(nombre__icontains=buscar) | Q(codigo__icontains=buscar))

    if request.method == 'POST':
        if not request.user.es_admin:
            return redirect('producto_list')

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        stock_actual = request.POST.get('stock_actual')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        proveedor_id = request.POST.get('proveedor')

        if codigo and nombre:
            try:
                producto = Producto.objects.create(
                    codigo=codigo,
                    nombre=nombre,
                    stock_actual=stock_actual or 0,
                    precio=precio or 0,
                )
                if categoria_id:
                    producto.categoria = Categoria.objects.get(id=categoria_id)
                if proveedor_id:
                    producto.proveedor = Proveedor.objects.get(id=proveedor_id)
                producto.save()
                return redirect('producto_list')
            except IntegrityError:
                pass

    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    contexto = {
        'productos': productos,
        'categorias': categorias,
        'proveedores': proveedores,
    }
    return render(request, 'inventario/productos.html', contexto)

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, id=pk)
    if request.method == 'POST':
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.stock_actual = request.POST.get('stock_actual')
        producto.precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        proveedor_id = request.POST.get('proveedor')

        if categoria_id:
            producto.categoria = Categoria.objects.get(id=categoria_id)
        else:
            producto.categoria = None

        if proveedor_id:
            producto.proveedor = Proveedor.objects.get(id=proveedor_id)
        else:
            producto.proveedor = None

        producto.save()
        return redirect('producto_list')

    categorias = Categoria.objects.all()
    proveedores = Proveedor.objects.all()
    context = {'producto': producto, 'categorias': categorias, 'proveedores': proveedores}
    return render(request, 'inventario/editar_producto.html', context)

@login_required
def eliminar_producto(request, pk):
    if not request.user.es_admin:
        return redirect('producto_list')
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'inventario/confirmar_eliminar.html', {'producto': producto, 'tipo': 'producto'})

@login_required
def movimiento_list(request):
    movimientos = Movimiento.objects.all().order_by('-fecha')
    productos = Producto.objects.all()
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        producto_id = request.POST.get('producto')
        tipo = request.POST.get('tipo')
        cantidad = int(request.POST.get('cantidad'))
        proveedor_id = request.POST.get('proveedor')
        observacion = request.POST.get('observacion')

        producto = get_object_or_404(Producto, pk=producto_id)
        proveedor = None
        if proveedor_id:
            proveedor = Proveedor.objects.get(id=proveedor_id)

        try:
            movimiento = Movimiento(
                producto=producto,
                usuario=request.user,
                tipo=tipo,
                cantidad=cantidad,
                proveedor=proveedor,
                observacion=observacion
            )
            movimiento.save()
            return redirect('movimiento_list')
        except ValueError as e:
            error = str(e)
            return render(request, 'inventario/movimientos.html', {
                'movimientos': movimientos,
                'productos': productos,
                'proveedores': proveedores,
                'error': error
            })

    context = {'movimientos': movimientos, 'productos': productos, 'proveedores': proveedores}
    return render(request, 'inventario/movimientos.html', context)

@login_required
def usuario_list(request):
    if not request.user.es_admin:
        return redirect('inicio')
    usuarios = Usuario.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        rol = request.POST.get('rol')
        if username and rol:
            Usuario.objects.create_user(username=username, rol=rol, password='123')
            return redirect('usuario_list')
    return render(request, 'inventario/usuarios.html', {'usuarios': usuarios})

@login_required
def categoria_list(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            try:
                Categoria.objects.create(nombre=nombre)
                return redirect('categoria_list')
            except IntegrityError:
                pass
    return render(request, 'inventario/categorias.html', {'categorias': categorias})

@login_required
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        producto_surte = request.POST.get('producto_surte')
        contacto = request.POST.get('contacto')
        if nombre:
            Proveedor.objects.create(nombre=nombre, producto_surte=producto_surte, contacto=contacto)
            return redirect('proveedor_list')
    return render(request, 'inventario/proveedores.html', {'proveedores': proveedores})
