from Modelo.productos.productoControl import ProductoControl
from Modelo.clientes.cliente import Cliente
class Factura(Cliente,ProductoControl):
    def __init__(self,nombreCliente,nombreProductos,productos,fecha,valorTotalCompra):
        super().__init__(nombreCliente,nombreProductos,productos)
        self.fecha = fecha
        self.valorTotalCompra = valorTotalCompra
