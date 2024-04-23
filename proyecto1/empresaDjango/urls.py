from django.urls import path

from empresaDjango import views

urlpatterns = [
    path('pedido/', views.index_pedido, name='index'),
    path('pedido/<int:cod_pedido>', views.detail_pedido, name='detail'),
    path('cliente/', views.index_cliente, name='index_cli'),
    path('cliente/<int:cif>', views.detail_cliente, name='detail_cli'),
    path('categoria/', views.index_categoria, name='index_cat'),
    path('categoria/<int:id_categoria>', views.detail_categoria, name='detail_cat'),

]