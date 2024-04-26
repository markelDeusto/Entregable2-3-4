from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.views import View

import empresaDjango
from empresaDjango.forms import PedidoForm, ProductoForm
from empresaDjango.models import Pedido, Cliente, Categoria, Producto, Componente


def index_pedido(request):
    pedidos = Pedido.objects.all()
    context = {'listado_pedidos' : pedidos}
    return render(request, 'index_pedido.html', context)


def detail_pedido(request, cod_pedido):
    pedido = Pedido.objects.select_related('cliente').get(pk=cod_pedido)
    return render(request, 'detail_pedido.html', {'pedido': pedido})

def index_cliente(request):
    clientes = Cliente.objects.all()
    output = ', '.join([c.cif for c in clientes])
    return HttpResponse(output)


def detail_cliente(request, cif):
    cliente = Cliente.objects.get(pk=cif)
    return HttpResponse(cliente)


def index_categoria(request):
    categorias = Categoria.objects.all()
    output = ', '.join([ca.nombre_categoria for ca in categorias])
    return HttpResponse(output)


def detail_categoria(request, id_categoria):
    categoria = Categoria.objects.get(pk=id_categoria)
    return HttpResponse(categoria)

def index_producto(request):
    productos = Producto.objects.all()
    output = ', '.join([pr.nombre_producto for pr in productos])
    return HttpResponse(output)


def detail_producto(request, cod_producto):
    producto = Producto.objects.get(pk=cod_producto)
    return HttpResponse(producto)

def index_componente(request):
    componentes = Componente.objects.all()
    output = ', '.join([co.nombre_componente for co in componentes])
    return HttpResponse(output)

def detail_componente(request, cod_componente):
    componente = Componente.objects.get(pk=cod_componente)
    return HttpResponse(componente)


class PedidoCreateView(View):
        def get(self, request):
            formulario =PedidoForm()
            context = {'formulario': formulario}
            return render(request, 'empresaDjango/pedido_create.html', context )
        def post(self, request):
            formulario = PedidoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                return redirect('index')#CAMBIAR
            return render(request, 'empresaDjango/pedido_create.html', {'formulario': formulario})



#class PedidoProductoCreateView(View):
 #   def get(self)

class ProductoCreateView(View):
    def get(self, request):
        formulario =ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'empresaDjango/producto_create.html', {'formulario': formulario})

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_pro')
        return render(request, 'empresaDjango/pedido_create.html', {'formulario': formulario})
