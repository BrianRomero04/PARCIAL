class Dispositivos:
    # Esta parte crea un "dispositivo" con sus detalles, como tipo, modelo, almacenamiento, etc.
    def __init__(self, tipo, modelo, almacenamiento, ram, procesador, pantalla, precioCompra):
        self.marca = "PHR"  
        self.tipo = tipo  
        self.modelo = modelo
        self.almacenamiento = almacenamiento  
        self.ram = ram  
        self.procesador = procesador  
        self.pantalla = pantalla  
        self.precioCompra = precioCompra
        self.precioVenta = self.calcuPrecioVenta()
        self.origen = "Importado"  

# Aquí calculamos el precio de venta multiplicando el precio de compra por 1.7.
    def calcuPrecioVenta(self):
        return self.precioCompra * 1.7

 # Esta parte muestra toda la información del dispositivo.
    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Almacenamiento: {self.almacenamiento}")
        print(f"RAM: {self.ram}")
        print(f"Procesador: {self.procesador}")
        print(f"Pantalla: {self.pantalla} pulgadas")
        print(f"Origen: {self.origen}")
        print(f"Precio de compra: ${self.precioCompra:.2f}")
        print(f"Precio de venta: ${self.precioVenta:.2f}")


# Creamos un dispositivo llamado "dispositivoa" con todos sus detalles específicos.
dispositivoa = Dispositivos(
    tipo="Tablet",
    modelo="PHR Note",
    almacenamiento="256GB",
    ram="16GB",
    procesador="Snapdragon ",
    pantalla=16,
    precioCompra=300
)

# Creamos otro dispositivo llamado "dispositivob" con sus propios detalles.
dispositivob = Dispositivos(
    tipo="Celular",
    modelo="PHR Estelar",
    almacenamiento="1Tb",
    ram="16GB",
    procesador="Snapdragon 3000",
    pantalla=6.6,
    precioCompra=400
)

# Mostramos la información de cada dispositivo.
dispositivoa.mostrar_informacion()
print()
dispositivob.mostrar_informacion()
