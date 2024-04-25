from django import forms

from empresaDjango.models import Pedido, Producto


class PedidoForm(forms.ModelForm):
        class Meta:
            model = Pedido
            fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'