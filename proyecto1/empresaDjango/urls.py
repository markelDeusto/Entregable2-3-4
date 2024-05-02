from django.urls import path

from empresaDjango import views
from empresaDjango.views import PedidoCreateView, ProductoCreateView, PedidoProductoCreateView, ClienteCreateView

urlpatterns = [
    path('pedido/', views.index_pedido, name='index_ped'),
    path('pedido/<int:cod_pedido>', views.detail_pedido, name='detail_ped'),
    path('cliente/', views.index_cliente, name='index_cli'),
    path('cliente/<int:cif>', views.detail_cliente, name='detail_cli'),
    path('categoria/', views.index_categoria, name='index_cat'),
    path('categoria/<int:id_categoria>', views.detail_categoria, name='detail_cat'),
    path('producto/', views.index_producto, name='index_pro'),
    path('producto/<int:cod_producto>', views.detail_producto, name='detail_pro'),
    path('componente/<int:cod_componente>', views.detail_componente, name='detail_com'),
    path('pedido/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('producto/create', ProductoCreateView.as_view(), name='producto_create'),
    path('pedidoproducto/create/<int:cod_pedido>/', PedidoProductoCreateView.as_view(), name='pedidoproducto_create'),
    path('cliente/create', ClienteCreateView.as_view(), name='cliente_create'),
    path('pedidoproducto/pregunta/<int:cod_pedido>/', views.ConfirmarProductoView.as_view(), name='pregunta'),
    path('pedido/borrar/<int:cod_pedido>', views.borrar_pedido, name="borrar_pedido"),
    path('producto/borrar/<int:cod_producto>', views.borrar_producto, name="borrar_producto"),
    path('pedido/actualizar/<int:cod_pedido>', views.actualizar_pedido.as_view(), name="actualizar_pedido"),
]
