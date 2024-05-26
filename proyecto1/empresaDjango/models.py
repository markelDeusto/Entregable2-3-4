from django.db import models


#Modelo de clientes
class Cliente(models.Model):
    cif = models.CharField(max_length=10, unique=True)
    nombre_empresa = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    contacto = models.CharField(max_length=10)

    def __str__(self):
        return f"nombre={self.nombre_empresa}"

#Modelo de pedidos
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_pedido = models.CharField(max_length=10, unique=True)
    fecha = models.DateField()
    precio_total = models.IntegerField(default=0)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return f"código={self.cod_pedido}, cliente={self.cliente.nombre_empresa}"

    #función para calcular el precio total
    def calcular_precio_total(self):
        precio_total = 0
        for producto_pedido in self.productopedido_set.all():
            precio_total += producto_pedido.producto.precio_unidad * producto_pedido.cantidad
        return precio_total

#Modelo de categorias
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"nombre={self.nombre_categoria}"

#Modelo de productos
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cod_producto = models.CharField(max_length=10, unique=True)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_unidad = models.IntegerField()
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return f"nombre={self.nombre_producto}, modelo={self.modelo}"

#Modelo de la relacion entre producto y pedido
class ProductoPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return (f"pedido={self.pedido.cod_pedido}, producto={self.producto.nombre_producto} {self.producto.modelo},"
                f" cantidad={self.cantidad}")

#Modelo de componentes
class Componente(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_componente = models.CharField(max_length=10, unique=True)
    nombre_componente = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return f"nombre={self.nombre_componente}"
