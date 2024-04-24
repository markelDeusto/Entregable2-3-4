from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from empresaDjango.models import Pedido, Cliente, Categoria, Producto, Componente


def index_pedido(request):
    pedidos = Pedido.objects.all()
    output = ', '.join([p.cod_pedido for p in pedidos])
    return HttpResponse(output)


def detail_pedido(request, cod_pedido):
    pedido = Pedido.objects.get(pk=cod_pedido)
    return HttpResponse(pedido)

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