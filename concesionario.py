class coches:
    # Esta parte crea un "coche" con todos sus detalles, como la marca, el modelo, el color, etc.
    def __init__(self, marca, modelo, año, color, tipo, motor, placa, tipoCombustible, precioCompra, origen):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo  
        self.motor = motor  
        self.placa = placa  
        self.tipoCombustible = tipoCombustible  
        self.precioCompra = precioCompra
        self.origen = origen  
        self.ruedas = 4
        self.capacidad_pasajeros = 5
        self.precio_venta = self.calcuPrecioVenta()

# Aquí calculamos el precio de venta multiplicando el precio de compra por 1.4.
    def calcuPrecioVenta(self):
        return self.precioCompra * 1.4

# Esta parte muestra toda la información del coche.
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo: {self.tipo}")
        print(f"Motor: {self.motor}")
        print(f"Placa: {self.placa}")
        print(f"Combustible: {self.tipoCombustible}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")
        print(f"Precio de compra: ${self.precioCompra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

# Creamos un coche llamado "autoa" con todos sus detalles específicos.
autoa = coches(
    marca="Mitsubishi",
    modelo="Lancer",
    año=2014,
    color="gris",
    tipo="Sedán",
    motor="1.8L",
    placa="P123-456",
    tipoCombustible="Gasolina",
    precioCompra=8000,
    origen="Nacional"
)

# Creamos otro coche llamado "autob" con sus propios detalles.
autob = coches(
    marca="Tesla",
    modelo="Cybertruck",
    año=2024,
    color="gris",
    tipo="SUV",
    motor="Electrico",
    placa="P2B4-2b2",
    tipoCombustible="Electricidad",
    precioCompra=80000,
    origen="Importado"
)

# Mostramos la información de cada coche.
autoa.mostrar_informacion()
print()
autob.mostrar_informacion()