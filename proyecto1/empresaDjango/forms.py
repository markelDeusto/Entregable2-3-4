from django import forms

from empresaDjango.models import Pedido, Producto, ProductoPedido, Cliente


class PedidoForm(forms.ModelForm):
        class Meta:
            model = Pedido
            fields = ['cliente', 'cod_pedido', 'fecha']
            widgets = {
                'fecha': forms.DateInput(attrs={'placeholder': 'Ejemplo: 2024-01-01'}),
            }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
