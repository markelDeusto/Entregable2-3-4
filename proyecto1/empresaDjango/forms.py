from django import forms

from empresaDjango.models import Pedido, Producto, ProductoPedido, Cliente, Componente
from .models import Categoria


# formulario de pedidos
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'cod_pedido', 'fecha']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'inputs-pedido'}),
            'cod_pedido': forms.TextInput(attrs={'class': 'inputs-pedido'}),
            'fecha': forms.DateInput(format="%d-%m-%Y", attrs={"type": "date", "class": "inputs-pedido"}),
        }


# formulario de productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'cod_producto', 'nombre_producto', 'descripcion', 'precio_unidad', 'modelo']
        widgets = {
            'categoria': forms.Select(attrs={'class': 'inputs-producto'}),
            'cod_producto': forms.TextInput(attrs={'class': 'inputs-producto'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'inputs-producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'inputs-producto'}),
            'precio_unidad': forms.NumberInput(attrs={'class': 'inputs-producto'}),
            'modelo': forms.TextInput(attrs={'class': 'inputs-producto'})
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['cod_producto'].error_messages = {
            'unique': 'Código de producto repetido, elige otro.'
        }


# formulario de la relacion entre productos y pedidos
class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'inputs-producto-pedido'}),
            'cantidad': forms.NumberInput(attrs={"class": "inputs-producto-pedido"})
        }


# formulario de clientes
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


# formulario de contacto (para email)
class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=10,
                             widget=forms.TextInput(attrs={'class': 'inputs-preguntas'}))
    email = forms.EmailField(label='Correo Electronico', required=True,
                             widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com',
                                                            'class': 'inputs-preguntas'}))
    mensaje = forms.CharField(label='Mensaje', required=True,
                              widget=forms.Textarea(attrs={'placeholder': 'Escribe tu duda aquí',
                                                           'class': 'inputs-preguntas'}))


# formulario de filtrado de productos
class FiltrarForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoria",
                                       required=False, label='Categoría')
    max_precio = forms.IntegerField(label='Precio maximo', min_value=0, required=False)


# formulario creacion del componente
class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['cod_componente', 'nombre_componente', 'marca']
