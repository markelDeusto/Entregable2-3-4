from django import forms

from empresaDjango.models import Pedido, Producto, ProductoPedido


class PedidoForm(forms.ModelForm):
        class Meta:
            model = Pedido
            fields = ['cliente', 'cod_pedido', 'fecha' ]



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = '__all__'
