import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directorio actual:",os.getcwd())

from ui import ui
menuGeneral= ui.menuGeneral()
menuProductos = ui.menuProductos()
menuClientes = ui.menuClientes()
from Modelo.productos.productoControl import ControlPlagas, ControlFertilizantes, Antibiotico
from Modelo.clientes.cliente import Cliente
from Modelo.pedidos.factura import Factura

from Crud.ImplCrudControlPlagas import ControlPlagas
from Crud.ImplCrudControlFertilizantes import ControlFertilizantes
from Crud.ImplCrudAntibiotico import Antibiotico
from Crud.ImplCrudCliente import Cliente

CrearProductoControlPlagas = ControlPlagas.crear
crearProductoControlFertilizante = ControlFertilizantes.crear
CrearAntibiotico = Antibiotico.crear
CrearCliente = Cliente.crear

"""
buscarCedula = Cliente.buscarCedula
mostrarFactura = Factura.mostrarFactura
"""
inventarioProductos = []
clientes = []
facturas = []
carritoDeCompras = [] # variable

#funciones buscar
def buscarProducto(registro): 
    print("\nBUSCADOR DE PRODUCTOS")
    for producto in inventarioProductos:
        if producto.registroICA == registro:
            print(f"Nombre producto: {producto.nombreProducto}")
            print(f"Registro ICA: {producto.registroICA}")
            print(f"Frecuencia de aplicación: {producto.frecuenciaAplicacion}")
            print(f"Valor del producto: {producto.valorProducto}")
            print(f"Cantidad de unidades disponibles: {producto.inventario}")
        else:
            print("No se han encontrado coincidencias. Intentalo nuevamente.")
            continue

def buscarCliente(cedula):
    print("\nBUSCADOR DE CLIENTES")
    for cliente in clientes:
        if cliente.cedula == cedula:
            print(f"Nombre cliente: {cliente.nombre}")
            print(f"Cedula cliente: {cliente.cedula}")
            Factura.mostrarFactura(cedula)
        else:
            print("No se han encontrado coincidencias. Intentalo nuevamente.")
            continue
            
# funciones crear
def crearProductoControl():
    CrearProductoControlPlagas('Phantom','444555','15 días',30.000,10,'plaga')
    inventarioProductos.append(CrearProductoControlPlagas)

    crearProductoControlFertilizante('Ghost','111222','30 días',80.300,16,'fertilizante')
    inventarioProductos.append(crearProductoControlFertilizante)
    print("Productos creados con éxito")
    
def crearAntibiotico():
    CrearAntibiotico('Acetaminofén',100.8,'Bovino',53.500,6)
    print("Antibiotico creado con éxito")

def crearCliente():
    CrearCliente('Octavio',123456789)
    clientes.append(CrearCliente)
    print("Cliente creado con éxito")

# funciones borrar
"""
def borrarProducto():
    
def borrarCliente():
    
def borrarFactura():
    
"""
# funcion para realizar una compra
def realizarNuevoPedido():
    if len(clientes) == 0:
        print("Debe crear al cliente antes de realizar el pedido.")
    cliente = None
    while cliente is None:
        cedulaCliente = input("Ingrese la cédula del cliente: ")
        cliente = next((cliente for cliente in clientes if cliente.cedula == cedulaCliente),None)
        if cliente is None:
            print("Cliente no encontrado. Intente nuevamente.")
        
    # Agregar productos al pedido
    procesoCompra = True
    subtotal = 0.0
    while procesoCompra:
        for producto in inventarioProductos:
            print(f"{producto}")
        seleccionarProducto = input("Ingrese el nombre del producto que desea agregar al carrito de compra: ")
        seleccionarCantidad = int(input("Ingrese cantidad de unidades que desea agregar al carrito de compra: "))
        
        for producto in inventarioProductos:
            if seleccionarProducto == producto.nombreProducto:
                subtotal += producto.valorProducto * seleccionarCantidad
                break
        print(f"El subtotal de su compra es: {subtotal}\n")
        auxAgregar = input("1. continuar agregando productos al carrito.\n2. finalizar compra.")
        if auxAgregar == '2':
            fecha = "2024-04-20"
            total = subtotal
            nuevoPedido = Factura(clientes.nombre,seleccionarProducto,fecha,total)
            facturas.append(nuevoPedido)

            procesoCompra = False # Finalizar proceso de compra
        else:
            print("Ingrese una opción válida.")
    print("Pedido realizado con éxito.")

while True:
    menuGeneral()
    option = input("Seleccione una opción: ")
    if option == "1":
        while True:
            menuProductos()
            opcionProductos = input("Seleccione una opción: ")
            if opcionProductos == '1':
                crearProductoControl()
            elif opcionProductos == '2':
                crearAntibiotico()
            elif opcionProductos == '3':
                1 #borrarProducto()
            elif opcionProductos == '4':
                registro = input("Ingrese registro ICA del producto: ")
                buscarProducto(registro)
            elif opcionProductos == '5':
                break #regresar al menu principal
            else:
                print("Ingrese una opción válida.")

    elif option == "2":
        while True:
            menuClientes()
            opcionClientes = input("Seleccione una opción: ")
            if opcionClientes == '1':
                crearCliente()
            elif opcionClientes == '2':
                1 #borrarCliente()
            elif opcionClientes == '3':
                buscarCliente()
            elif opcionClientes == '4':
                break #regresar al menu principal
            else:
                print("Ingrese una opción válida.")

    elif option == "3":
        realizarNuevoPedido()
    elif option == "4":
        print("Sistema cerrado.")
        break #salir del programa principal.
    else:
        print("Opción no válida. Inténtelo nuevamente")
