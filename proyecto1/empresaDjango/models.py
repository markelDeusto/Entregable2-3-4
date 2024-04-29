from django.db import models


# Create your models here.
class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    contacto = models.CharField(max_length=10)

    def __str__(self):
        return f"cif={self.cif}, nombre={self.nombre_empresa}, dirección={self.direccion}, contacto={self.contacto}"



class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_pedido = models.CharField(max_length=10)
    fecha = models.DateField()
    precio_total = models.IntegerField(default=0)

    def __str__(self):
        return f"código={self.cod_pedido}, cliente={self.cliente.nombre_empresa}, fecha={self.fecha}, precio={self.precio_total}€"


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"id={self.id_categoria}, nombre={self.nombre_categoria}"


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cod_producto = models.CharField(max_length=10)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_unidad = models.IntegerField()
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return (f"nombre={self.nombre_producto}, modelo={self.modelo}, categoria={self.categoria.nombre_categoria}, "
                f"precio={self.precio_unidad}, código={self.cod_producto}, descripcion={self.descripcion}")


class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return (f"pedido={self.pedido.cod_pedido}, producto={self.producto.nombre_producto} {self.producto.modelo},"
                f" cantidad={self.cantidad}")


class Componente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_componente = models.CharField(max_length=10)
    nombre_componente = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return (f"nombre={self.nombre_componente}, código={self.cod_componente}, marca={self.marca}, "
                f"producto={self.producto.nombre_producto} {self.producto.modelo}")
