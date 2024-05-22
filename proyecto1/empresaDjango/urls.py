from django.urls import path

from empresaDjango import views
from empresaDjango.views import PedidoCreateView, ProductoCreateView, PedidoProductoCreateView, ClienteCreateView

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('pedido/', views.index_pedidoListView.as_view(), name='index_ped'),
    path('pedido/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('pedido/<str:cod_pedido>', views.detail_pedido, name='detail_ped'),
    path('cliente/', views.index_cliente, name='index_cli'),
    path('cliente/create', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/<str:cif>', views.detail_cliente, name='detail_cli'),
    path('categoria/<str:id_categoria>', views.detail_categoria, name='detail_cat'),
    path('producto/', views.index_productoListView.as_view(), name='index_pro'),
    path('producto/create', ProductoCreateView.as_view(), name='producto_create'),
    path('producto/<str:cod_producto>', views.detail_producto, name='detail_pro'),
    path('componente/<str:cod_componente>', views.detail_componente, name='detail_com'),
    path('pedidoproducto/create/<str:cod_pedido>/', PedidoProductoCreateView.as_view(), name='pedidoproducto_create'),
    path('pedidoproducto/pregunta/<str:cod_pedido>/', views.ConfirmarProductoView.as_view(), name='pregunta'),
    path('pedido/borrar/<str:cod_pedido>', views.borrar_pedido, name="borrar_pedido"),
    path('producto/borrar/<str:cod_producto>', views.borrar_producto, name="borrar_producto"),
    path('pedido/actualizar/<str:cod_pedido>', views.actualizar_pedido.as_view(), name="actualizar_pedido"),
    path('pedido/actualizar/producto/<str:cod_pedido>', views.actualizar_productoEnPedido.as_view(),
         name="actualizar_productoEnPedido"),
    path('contacto', views.contacto, name="contacto"),
]
