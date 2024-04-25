import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directiorio actual:",os.getcwd())

from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes, Antibiotico
from Modelo.clientes.cliente import Cliente
from Modelo.pedidos.factura import Factura

guardarCliente = Cliente.registrarCliente
cliente = Cliente

guardarFactura = Factura.registrarFactura
factura = Factura

guardarProductoControl = ProductoControl.registrarProducto
productoPlagas = ControlPlagas
productoFertilizante = ControlFertilizantes

guardarAntibiotico = Antibiotico.registrarAntibiotico
antibiotico = Antibiotico

# 1. crear en el crud las funciones y los casos de prueba: 3 clientes, 3 fertilizantes, 3 control de plagas y 3 antibioticos -> 3 facturas respectivamente

def crearCliente():
    nombre = "Octavio"
    cedula = "123456789"
    nuevoCliente = cliente(nombre,cedula)
    guardarCliente(nuevoCliente)
    print("Cliente creado con exito.")

def crearProductoControl():
    nombre = ""
    registroICA = ""
    frecuenciaAplicacion = ""
    valorProducto = float()
    disponibleInventario = int()
    tipoProducto = "" #Control de plagas o fertilizantes

    if tipoProducto == "plaga":
        periodoCarencia = int()
        nuevoProducto = productoPlagas(nombre,registroICA,frecuenciaAplicacion,valorProducto,disponibleInventario,periodoCarencia)
        guardarProductoControl(nuevoProducto)
        print("Producto creado con éxito.")

    elif tipoProducto == "fertilizante":
        ultimaAplicacion = "" #Fecha formato (YYYY-MM-DD)
        nuevoProducto = productoFertilizante(nombre,registroICA,frecuenciaAplicacion,valorProducto,disponibleInventario,ultimaAplicacion)
        guardarProductoControl(nuevoProducto)
        print("Producto creado con éxito.")

def crearAntibiotico():
    nombre = ""
    dosis = float()
    tipoAnimal = "(Bovinos/Caprinos/Porcinos)"
    valorProducto = float()
    disponibleInventario = int()
    nuevoAntibiotico = antibiotico(nombre,dosis,tipoAnimal,valorProducto,disponibleInventario)
    guardarAntibiotico(nuevoAntibiotico)
    print("Antibiótico creado con éxito")

def crearFactura(): 
    nombreCliente = ""
    listaProductos = []
    fecha = ""
    valorTotalCompra = float()
    nuevaFactura = factura(nombreCliente,listaProductos,fecha,valorTotalCompra)
    guardarFactura(nuevaFactura)
