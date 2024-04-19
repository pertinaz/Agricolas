class ProductoControl:
    def __init__(self,registroICA,nombreProducto,frecuenciaAplicacion,valorProducto):
        self.registroICA = registroICA
        self.nombreProducto = nombreProducto
        self.frecuenciaAplicacion = frecuenciaAplicacion # (es decir, cada cuanto periodo se aplica el producto.Cada 15 días, cada 30 días, etc)
        self.valorProducto = valorProducto

class ControlPlagas(ProductoControl):
    def __init__(self,registroICA
    ,nombreProducto,frecuenciaAplicacion,valorProducto,periodoCarencia):
        super().__init__(registroICA,nombreProducto,frecuenciaAplicacion, valorProducto)
        self.periodoCarencia = periodoCarencia # (es el tiempo legalmenteestablecido, expresado usualmente en número de días que debe transcurrir entre la última aplicación de un fitosanitario y la cosecha)

class ControlFertilizantes(ProductoControl):
    def __init__(self,registroICA,nombreProducto,frecuenciaAplicacion,valorProducto,fechaUltimaAplicacion):
        super().__init__(registroICA,nombreProducto,frecuenciaAplicacion,valorProducto)
        self.fechaUltimaAplicacion = fechaUltimaAplicacion

class Antibiotico:
    def __init__(self,nombreProducto,dosis,tipoAnimal,precio):
        self.nombreProducto = nombreProducto
        self.dosis = dosis
        self.tipoAnimal = tipoAnimal
        self.precio = precio