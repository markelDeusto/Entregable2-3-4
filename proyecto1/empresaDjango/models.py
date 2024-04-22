from django.db import models


# Create your models here.
class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    contacto = models.CharField(max_length=10)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_pedido = models.CharField(max_length=10)
    fecha = models.DateField()
    precio_total = models.IntegerField()

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cod_producto = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_unidad = models.IntegerField()
    modelo = models.CharField(max_length=50)

class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Componente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_componente = models.CharField(max_length=10)
    nombre_componente = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

