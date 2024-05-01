from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import View

import empresaDjango
from empresaDjango.forms import PedidoForm, ProductoForm, ProductoPedidoForm, ClienteForm
from empresaDjango.models import Pedido, Cliente, Categoria, Producto, Componente, ProductoPedido


def index_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'index_pedido.html', {'listado_pedidos' : pedidos})


def detail_pedido(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)
    detalles_pedido = ProductoPedido.objects.filter(pedido=pedido)
    context = {
        'pedido' : pedido,
        'detalles_pedido' : detalles_pedido,
    }
    return render(request, 'detail_pedido.html', context)

def index_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'index_cliente.html', {'listado_clientes' : clientes})


def detail_cliente(request, cif):
    cliente = get_object_or_404(Cliente, cif=cif)
    context = {
        'cliente' : cliente
    }
    return render(request, 'detail_cliente.html', context)


def index_categoria(request):
    categorias = Categoria.objects.all()
    output = ', '.join([ca.nombre_categoria for ca in categorias])
    return HttpResponse(output)


def detail_categoria(request, id_categoria):
    categoria = Categoria.objects.get(pk=id_categoria)
    return HttpResponse(categoria)

def index_producto(request):
    productos = Producto.objects.all()
    return render(request, 'index_producto.html', {'listado_productos': productos})


def detail_producto(request, cod_producto):
    producto = get_object_or_404(Producto, cod_producto=cod_producto)
    componentes = Componente.objects.filter(producto=producto)
    context = {
        'producto': producto,
        'componentes': componentes,
    }
    return render(request, 'detail_producto.html', context)

def detail_componente(request, cod_componente):
    componente = get_object_or_404(Componente, cod_componente=cod_componente)
    context = {
        'componente': componente
    }
    return render(request, 'detail_componente.html', context)


class PedidoCreateView(View):
        def get(self, request):
            formulario=PedidoForm()
            context = {'formulario': formulario}
            return render(request, 'pedido_create.html', context)
        def post(self, request):
            formulario = PedidoForm(data=request.POST)
            if formulario.is_valid():
                pedido=formulario.save()
                cod_pedido = pedido.cod_pedido
                return redirect('pedidoproducto_create', cod_pedido=cod_pedido)
            return render(request, 'pedido_create.html', {'formulario': formulario})



class ProductoCreateView(View):
    def get(self, request):
        formulario =ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'producto_create.html', {'formulario': formulario})

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_pro')
        return render(request, 'producto_create.html', {'formulario': formulario})

class PedidoProductoCreateView(View):
    def get(self,request, cod_pedido):
        formulario = ProductoPedidoForm()
        context = {'formulario': formulario, 'cod_pedido': cod_pedido}
        return render(request, 'empresaDjango/producto_pedido.html', {'formulario': formulario, 'cod_pedido': cod_pedido})

    def post(self,request, cod_pedido):
        formulario = ProductoPedidoForm(data=request.POST)
        if formulario.is_valid():
       #     pedido = Pedido.objects.get(cod_pedido=cod_pedido)
       #     productos_pedido = ProductoPedido.objects.filter(pedido=pedido)
       #     precio_total_pedido = sum(
        #        producto_pedido.producto.precio * producto_pedido.cantidad for producto_pedido in productos_pedido)
#
            # Guardar el precio total en el pedido
 #           pedido.precio_total = precio_total_pedido
  #          pedido.save()
            formulario.save()
        return render(request, 'empresaDjango/producto_pedido.html', {'formulario':  formulario})

class ClienteCreateView(View):
    def get(self, request):
        formulario = ClienteForm()
        context = {'formulario': formulario}
        return render(request, 'cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_cli')
        return render(request, 'cliente_create.html', {'formulario': formulario})
