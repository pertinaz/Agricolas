import os
print("Directiorio actual:",os.getcwd())
from Modelo.productos.productoControl import ProductoControl, ControlPlagas, ControlFertilizantes, Antibiotico
from Modelo.clientes.cliente import Cliente
from Modelo.pedidos.factura import Factura

def menu():
    print("\nMENU\n")
    print("1. Crear nuevo producto de control")
    print("2. Crear nuevo antibiótico")
    print("3. Crear nuevo cliente")
    print("4. Realizar nuevo pedido")
    print("5.Salir")

productos = []
clientes = []
pedidos = []

while True:
    menu()
    option = input("Seleccione una opción: ")

    if option == "1":
        nombre = input("Ingrese el nombre del producto de control: ")
        registroICA = input("Ingrese el registro ICA del producto: ")
        frecuenciaAplicacion = input("Ingrese la frecuencia de aplicación del producto: ")
        valorProducto = float(input("Ingrese el valor del producto: "))
        tipoProducto = input("Ingrese el tipo de producto (Control de plagas/Fertilizantes): ").lower()

        if tipoProducto == "plaga":
            periodoCarencia = int(input("Ingrese el periodo de carencia del producto (en dias): "))
            nuevoProducto = ControlPlagas(registroICA,nombre,frecuenciaAplicacion,valorProducto,periodoCarencia
            )
        
        if tipoProducto == "fertilizante":
            ultimaAplicacion = input("Ingrese la fecha de la última aplicación del producto (YYYY-MM-DD): ")
            nuevoProducto = ControlFertilizantes(registroICA,nombre,frecuenciaAplicacion,valorProducto,ultimaAplicacion
            )
        else:
            print("Tipo de producto no válido.")
            continue
        productos.append(nuevoProducto)
        print("Producto creado con éxito.")
    elif option == "2":
        nombre = input("Ingrese el nombre del antibiótico: ")
        dosis = float(input("Ingrese la dosis del antibiótico (entre 400 y 600 Kg): "))
        tipoAnimal = input("Ingrese el tipo de animal al que se puede aplicar (Bovinos/Caprinos/Porcinos): ")
        precio = float(input("Ingrese el precio del antibiótico: "))
        nuevoAntibiotico = Antibiotico(nombre,dosis,tipoAnimal,precio)
        productos.append(nuevoAntibiotico)
        print("Antibiótico creado con éxito")
    elif option == "3":
        nombre = input("Ingrese el nombre del cliente: ")
        cedula = input("Ingrese la cedula del cliente: ")
        nuevoCliente = Cliente(nombre,cedula)
        clientes.append(nuevoCliente)
        print("Cliente creado con éxito")
    elif option == "4":
        if len(clientes) == 0:
            print("Crear al cliente antes de realizar el pedido.")
            continue
        cliente = None
        while cliente is None:
            cedulaCliente = input("Ingrese la cédula del cliente: ")
            cliente = next((cliente for cliente in clientes if cliente.cedula == cedulaCliente),None)
            if cliente is None:
                print("Cliente no encontrado. Intente nuevamente.")
        
        print("Pedido realizado con éxito.")
    elif option == "5":
        print("Sistema cerrado.")
        break
    else:
        print("Opción no válida. Inténtelo nuevamente")