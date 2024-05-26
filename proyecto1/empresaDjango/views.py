from django.core.mail.backends import console
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import UpdateView, ListView

from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages

from django.conf import settings

import empresaDjango
from empresaDjango.forms import PedidoForm, ProductoForm, ProductoPedidoForm, ClienteForm, ContactoForm, FiltrarForm
from empresaDjango.models import Pedido, Cliente, Categoria, Producto, Componente, ProductoPedido

from django.core.mail import EmailMessage
from django.http import JsonResponse


def landing_page(request):
    return render(request, 'landing_page.html')

class index_pedidoListView(ListView):
    model = Pedido
    template_name = 'index_pedido.html'
    context_object_name = 'listado_pedidos'
    paginate_by = 5


def detail_pedido(request, cod_pedido):
    pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)
    precio_total = pedido.calcular_precio_total()
    pedido.precio_total = precio_total
    pedido.save()
    detalles_pedido = ProductoPedido.objects.filter(pedido=pedido)
    context = {
        'pedido': pedido,
        'detalles_pedido': detalles_pedido,
    }
    return render(request, 'detail_pedido.html', context)

def actualizar_estado_pedido(request, cod_pedido):
    if request.method == 'POST':
        try:
            pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)
            data = json.loads(request.body)
            estado = data.get('estado', 'False')
            pedido.estado = estado  # Asegúrate de que el modelo Pedido tiene un campo 'estado'
            pedido.save()
            return JsonResponse({'status': 'success'})
        except Pedido.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Pedido no encontrado'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)

def borrar_pedido(request, cod_pedido):
    pedido = Pedido.objects.get(cod_pedido=cod_pedido)
    pedido.delete()
    return redirect('index_ped')


class actualizar_pedido(UpdateView):
    model = Pedido

    def get(self, request, cod_pedido):
        pedido = Pedido.objects.get(cod_pedido=cod_pedido)
        formulario = PedidoForm(instance=pedido)
        context = {
            'formulario': formulario,
            'pedido': pedido,
            'cod_pedido': cod_pedido
        }
        return render(request, 'update_pedido.html', context)

    def post(self, request, cod_pedido):
        pedido = Pedido.objects.get(cod_pedido=cod_pedido)
        formulario = PedidoForm(request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_ped')
        else:
            formulario = PedidoForm(instance=pedido)
        return render(request, 'update_pedido.html', {'formulario': formulario})




class actualizar_productoEnPedido(UpdateView):
    model = ProductoPedido

    def get(self, request, cod_pedido):
        productoPedido = ProductoPedido.objects.get(pedido__cod_pedido=cod_pedido)
        formulario = ProductoPedidoForm(instance=productoPedido)
        context = {
            'formulario': formulario,
            'productoPedido': productoPedido,
            'cod_pedido': cod_pedido
        }
        return render(request, 'update_productoEnPedido.html', context)

    def post(self, request, cod_pedido):
        productoPedido = ProductoPedido.objects.get(pedido__cod_pedido=cod_pedido)
        formulario = ProductoPedidoForm(request.POST, instance=productoPedido)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_ped')
        else:
            formulario = ProductoPedidoForm(instance=productoPedido)
        return render(request, 'update_productoEnPedido.html', {'formulario': formulario})


def index_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'index_cliente.html', {'listado_clientes': clientes})


def detail_cliente(request, cif):
    cliente = get_object_or_404(Cliente, cif=cif)
    context = {
        'cliente': cliente
    }
    return render(request, 'detail_cliente.html', context)

def borrarcliente(request, cif):
    cliente = Cliente.objects.get(cif=cif)
    cliente.delete()
    return redirect('index_cli')

def detail_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoria, id_categoria=id_categoria)
    context = {
        'categoria': categoria
    }
    return render(request, 'detail_categoria.html', context)


class index_productoListView(ListView):
    model = Producto
    formulario = ProductoForm
    template_name = 'index_producto.html'
    context_object_name = 'listado_productos'
    paginate_by = 5

    def get_queryset(self):
        productos = Producto.objects.all()
        self.formulario = FiltrarForm(self.request.GET)
        if self.formulario.is_valid():
            id_categoria = self.formulario.cleaned_data.get('categoria')
            max_precio = self.formulario.cleaned_data.get('max_precio')
            if id_categoria:
                productos = productos.filter(categoria_id=id_categoria)
            if max_precio is not None:
                productos = productos.filter(precio_unidad__lt=max_precio)
        return productos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = self.formulario
        return context


def detail_producto(request, cod_producto):
    producto = get_object_or_404(Producto, cod_producto=cod_producto)
    componentes = Componente.objects.filter(producto=producto)
    context = {
        'producto': producto,
        'componentes': componentes,
    }
    return render(request, 'detail_producto.html', context)


def borrar_producto(request, cod_producto):
    producto = Producto.objects.get(cod_producto=cod_producto)
    producto.delete()
    return redirect('index_pro')


def detail_componente(request, cod_componente):
    componente = get_object_or_404(Componente, cod_componente=cod_componente)
    context = {
        'componente': componente
    }
    return render(request, 'detail_componente.html', context)


class PedidoCreateView(View):
    def get(self, request):
        formulario = PedidoForm()
        context = {'formulario': formulario}
        return render(request, 'pedido_create.html', context)

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            pedido = formulario.save()
            cod_pedido = pedido.cod_pedido
            return redirect('pedidoproducto_create', cod_pedido=cod_pedido)
        return render(request, 'pedido_create.html', {'formulario': formulario})


class ProductoCreateView(View):
    def get(self, request):
        formulario = ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'producto_create.html', context)

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index_pro')
        return render(request, 'producto_create.html', {'formulario': formulario})


class PedidoProductoCreateView(View):
    def get(self, request, cod_pedido):
        formulario = ProductoPedidoForm()
        context = {'formulario': formulario, 'cod_pedido': cod_pedido}
        return render(request, 'producto_pedido.html', context)

    def post(self, request, cod_pedido):
        pedido = get_object_or_404(Pedido, cod_pedido=cod_pedido)
        formulario = ProductoPedidoForm(data=request.POST)
        if formulario.is_valid():
            producto_pedido = formulario.save(commit=False)
            producto_pedido.pedido = pedido
            producto_pedido.save()
            return redirect('pregunta', cod_pedido=cod_pedido)
        return render(request, 'producto_pedido.html', {'formulario': formulario, 'cod_pedido': cod_pedido})


class ConfirmarProductoView(View):
    def get(self, request, cod_pedido):
        return render(request, 'producto_pedido_pregunta.html', {'cod_pedido': cod_pedido})

    def post(self, request, cod_pedido):
        opcion = request.POST.get('opcion')
        if opcion == "SI":
            return redirect('pedidoproducto_create', cod_pedido=cod_pedido)
        else:
            return redirect('index_ped')


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


def contacto(request):
    contacto_form = ContactoForm()
    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)
        if contacto_form.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')

            send_mail(
                'Confirmación de recepción de email',
                'Hola ' + nombre + ':' + '\n' + 'Hemos recibido tu consulta con el siguiente mensaje: ' + '\n' + mensaje +
                '\n' + 'Nos pondremos en contacto con usted para resolver la duda lo antes posible.' + '\n' + '\n'
                + 'Atentamente, el equipo de Deustronic.',
                'settings.EMAIL_HOST_USER',
                [email],
            )
            fail_silently = False
            return redirect('contacto')

    return render(request, 'contactanos.html', {"contacto_form": contacto_form})
