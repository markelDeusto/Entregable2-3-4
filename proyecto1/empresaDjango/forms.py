from django import forms

from empresaDjango.models import Pedido, Producto, ProductoPedido, Cliente
from .models import Categoria


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'cod_pedido', 'fecha', 'estado']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'inputs-pedido'}),
            'cod_pedido': forms.TextInput(attrs={'class': 'inputs-pedido'}),
            'fecha': forms.DateInput(format="%d-%m-%Y", attrs={"type": "date", "class": "inputs-pedido"}),
            'estado': forms.Select(attrs={'class': 'inputs-pedido'}),
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = ['producto','cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'inputs-producto-pedido'}),
            'cantidad': forms.NumberInput(attrs={"class": "inputs-producto-pedido"})
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=10, widget=forms.TextInput(attrs={'class': 'inputs-preguntas'}))
    email = forms.EmailField(label='Correo Electronico', required=True, widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com',
                                                                                                       'class': 'inputs-preguntas'}))
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'placeholder': 'Escribe tu duda aquí',
                                                                                           'class': 'inputs-preguntas'}))

class FiltrarForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecciona una categoria",
                                       required=False, label='Categoría')
    max_precio = forms.IntegerField(label='Precio maximo', min_value=0, required=False)
