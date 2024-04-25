class ProductoControl:
    def __init__(self,registroICA,nombreProducto,frecuenciaAplicacion,valorProducto,inventario):
        self.registroICA = registroICA
        self.nombreProducto = nombreProducto
        self.frecuenciaAplicacion = frecuenciaAplicacion # (es decir, cada cuanto periodo se aplica el producto.Cada 15 días, cada 30 días, etc)
        self.valorProducto = valorProducto
        self.inventario = inventario

        self.__productosDisponibles = []

    @property
    def productosDisponibles(self):
        return self.__productosDisponibles
    
    @productosDisponibles.setter
    def productosDisponibles(self,producto):
        self.__productosDisponibles.append(producto)

    def registrarProducto(self,producto):
        self.__productosDisponibles = producto
        
class ControlPlagas(ProductoControl):
    def __init__(self,registroICA
    ,nombreProducto,frecuenciaAplicacion,valorProducto,inventario,periodoCarencia):
        super().__init__(registroICA,nombreProducto,frecuenciaAplicacion, valorProducto,inventario)
        self.periodoCarencia = periodoCarencia # (es el tiempo legalmenteestablecido, expresado usualmente en número de días que debe transcurrir entre la última aplicación de un fitosanitario y la cosecha)

class ControlFertilizantes(ProductoControl):
    def __init__(self,registroICA,nombreProducto,frecuenciaAplicacion,valorProducto,inventario,fechaUltimaAplicacion):
        super().__init__(registroICA,nombreProducto,frecuenciaAplicacion,valorProducto,inventario)
        self.fechaUltimaAplicacion = fechaUltimaAplicacion

class Antibiotico:
    def __init__(self,nombreProducto,dosis,tipoAnimal,precio,inventario):
        self.nombreProducto = nombreProducto
        self.dosis = dosis
        self.tipoAnimal = tipoAnimal
        self.precio = precio
        self.inventario = inventario

        self.__antibioticos = []
        
    @property
    def antibioticos(self):
        return self.__antibioticosDisponibles
    
    @antibioticos.setter
    def antibioticos(self,producto):
        self.__antibioticosDisponibles.append(producto)

    def registrarAntibiotico(self,producto):
        self.__antibioticosDisponibles = producto
