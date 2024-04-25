import sys
sys.path.append('c:/Users/Czsgt_/Documents/UTP/PROGIII - cleanCodeModule/Proyecto python Segundo parcial/Agricolas')
import os
print("Directorio actual:",os.getcwd())

from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes, Antibiotico
from Modelo.clientes.cliente import Cliente
from Modelo.pedidos.factura import Factura

buscarCedula = Cliente.buscarCedula
mostrarFactura = Factura.mostrarFactura

productos = []
clientes = []
pedidos = []

def menu():
    print("\nMENU\n")
    print("1. Crear nuevo producto de control")
    print("2. Crear nuevo antibiótico")
    print("3. Crear nuevo cliente")
    print("4. Realizar nuevo pedido")
    print("5. Ver informacion cliente")

    print("6. Salir")

def listaProductos():
    print("\nLISTA DE PRODUCTOS")
    n=0
    for producto in productos:
        for nombreProducto in producto:     
            print(f"{n+1}.{nombreProducto}")
            disponibles = producto.count()
            print(f"Cantidad de unidades disponibles: {disponibles}")

def crearProductoControl():
    nombre = input("Ingrese el nombre del producto de control: ")
    registroICA = input("Ingrese el registro ICA del producto: ")
    frecuenciaAplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
    valorProducto = float(input("Ingrese el valor del producto: "))
    disponibleInventario = int(input("Ingrese la cantidad de unidades: "))
    tipoProducto = input("Ingrese el tipo de producto (Control de plagas/Fertilizantes): ").lower()

    if tipoProducto == "plaga":
        periodoCarencia = int(input("Ingrese el periodo de carencia del producto (en dias): "))
        nuevoProducto = ControlPlagas(registroICA,nombre,frecuenciaAplicacion,valorProducto,disponibleInventario,periodoCarencia
        )
    
    elif tipoProducto == "fertilizante":
        ultimaAplicacion = input("Ingrese la fecha de la última aplicación del producto (YYYY-MM-DD): ")
        nuevoProducto = ControlFertilizantes(registroICA,nombre,frecuenciaAplicacion,valorProducto,disponibleInventario,ultimaAplicacion
        )
    else:
        print("Tipo de producto no válido.")
    productos.append(nuevoProducto)
    print("Producto creado con éxito.")

def crearNuevoAntibiotico():
    nombre = input("Ingrese el nombre del antibiótico: ")
    dosis = float(input("Ingrese la dosis del antibiótico (entre 400 y 600 Kg): "))
    tipoAnimal = input("Ingrese el tipo de animal al que se puede aplicar (Bovinos/Caprinos/Porcinos): ")
    valorProducto = float(input("Ingrese el precio del antibiótico: "))
    disponibleInventario = int(input("Ingrese la cantidad de unidades: "))
    nuevoAntibiotico = Antibiotico(nombre,dosis,tipoAnimal,valorProducto,disponibleInventario)
    productos.append(nuevoAntibiotico)
    print("Antibiótico creado con éxito")

def crearNuevoCliente():
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cedula del cliente: ")
    nuevoCliente = Cliente(nombre,cedula)
    clientes.append(nuevoCliente)
    print("Cliente creado con éxito")

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
        listaProductos()
        seleccionarProducto = input("Ingrese el nombre del producto que desea agregar al carrito de compra: ")
        seleccionarCantidad = int(input("Ingrese cantidad de unidades que desea agregar al carrito de compra: "))
        
        for producto in productos:
            if seleccionarProducto == producto.nombreProducto:
                subtotal += producto.valorProducto * seleccionarCantidad
                break
        print(f"El subtotal de su compra es: {subtotal}\n")
        auxAgregar = input("1. continuar agregando productos al carrito.\n2. finalizar compra.")
        if auxAgregar == '2':
            fecha = "2024-04-20"
            total = subtotal
            nuevoPedido = Factura(clientes.nombre,seleccionarProducto,fecha,total)
            pedidos.append(nuevoPedido)

            procesoCompra = False # Finalizar proceso de compra
        else:
            print("Ingrese una opción válida.")
    print("Pedido realizado con éxito.")

def historialCliente():
    cedula = int(input("Cedula cliente: "))
    if buscarCedula(cedula):
        mostrarFactura(cedula)


while True:
    menu()
    option = input("Seleccione una opción: ")
    if option == "1":
        crearProductoControl()
    elif option == "2":
        crearNuevoAntibiotico()
    elif option == "3":
        crearNuevoCliente()
    elif option == "4":
        realizarNuevoPedido()
    elif option == "5":
        historialCliente() # buscar por cedula
    elif option == "6":
        print("Sistema cerrado.")
        break
    else:
        print("Opción no válida. Inténtelo nuevamente")
