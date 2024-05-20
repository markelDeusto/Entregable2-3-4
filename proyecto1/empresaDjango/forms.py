from django import forms

from empresaDjango.models import Pedido, Producto, ProductoPedido, Cliente
from .models import Categoria


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'cod_pedido', 'fecha']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'inputs-pedido'}),
            'cod_pedido': forms.TextInput(attrs={'class': 'inputs-pedido'}),
            'fecha': forms.DateInput(format="%d-%m-%Y", attrs={"type": "date", "class": "inputs-pedido"})
        }



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProductoPedido
        fields = '__all__'
        widgets = {
            'producto': forms.Select(attrs={'class': 'inputs-producto-pedido'}),
            'pedido': forms.Select(attrs={'class': 'inputs-producto-pedido'}),
            'cantidad': forms.NumberInput(attrs={"class": "inputs-producto-pedido"})
        }


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=10)
    email = forms.EmailField(label='Correo Electronico', required=True, widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com'}))
    mensaje = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea)

class FiltarForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, label='Categoría')