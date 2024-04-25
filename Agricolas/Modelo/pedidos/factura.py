import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directiorio actual:",os.getcwd())
from Modelo.clientes.cliente import Cliente
from Modelo.productos.productoControl import ProductoControl
buscarCedula = Cliente.buscarCedula

class Factura(Cliente,ProductoControl):
    def __init__(self,nombreCliente,cedulaCliente,nombreProductos,fecha,valorTotalCompra):
        super().__init__(nombreCliente,cedulaCliente,nombreProductos)
        self.fecha = fecha
        self.valorTotalCompra = valorTotalCompra

        self.__facturas = [] # Getter y setter crear el metodo asociar para añadir las facturas a una lista de facturas o base de datos

    @property
    def facturas(self):
        return self.__facturas

    @facturas.setter
    def facturas(self,factura):
        self.__facturas.append(factura)
    
    def registrarFactura(self,factura):
        self.__facturas = factura
    
    def mostrarFactura(self,cedulaCliente):
        if buscarCedula(cedulaCliente):
            for cedula in self.__facturas.cedulaCliente:
                if cedulaCliente == cedula:
                    return (f"HISTORIAL ASOCIADO: \n{self.__facturas}")
                else:
                    raise ValueError(f"El cliente no tiene facturas asociadas aún...")
        else:
            raise ValueError(f"No existe tal cliente con cedula: {cedulaCliente}")
