from django.urls import path

from empresaDjango import views
from empresaDjango.views import PedidoCreateView, ProductoCreateView

urlpatterns = [
    path('pedido/', views.index_pedido, name='index_ped'),
    path('pedido/<int:cod_pedido>', views.detail_pedido, name='detail_ped'),
    path('cliente/', views.index_cliente, name='index_cli'),
    path('cliente/<int:cif>', views.detail_cliente, name='detail_cli'),
    path('categoria/', views.index_categoria, name='index_cat'),
    path('categoria/<int:id_categoria>', views.detail_categoria, name='detail_cat'),
    path('producto/', views.index_producto, name='index_pro'),
    path('producto/<int:cod_producto>', views.detail_producto, name='detail_pro'),
    path('componente/', views.index_componente, name='index_com'),
    path('componente/<int:cod_componente>', views.detail_componente, name='detail_pro'),
    path('/pedido/create', PedidoCreateView.as_view(), name='pedido_create'),
    path('/producto/create', ProductoCreateView.as_view(), name='producto_create')
]