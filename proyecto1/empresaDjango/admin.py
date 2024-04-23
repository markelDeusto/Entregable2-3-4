from django.contrib import admin

from empresaDjango.models import Cliente, Categoria, Componente, Pedido, Producto, ProductoPedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Componente)
admin.site.register(Pedido)
admin.site.register(Producto)
admin.site.register(ProductoPedido)
