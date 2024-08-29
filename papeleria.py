class objetos:
    # Esta parte crea un "objeto" con el precio de compra y calcula el precio de venta.
    def __init__(self, precioCompra):
        self.precioCompra = precioCompra
        self.precio_venta = self.calcuPrecioVenta()# Calculamos el precio de venta de una vez.
# Aquí multiplicamos el precio de compra por 1.30 para obtener el precio de venta.
    def calcuPrecioVenta(self):
        return self.precioCompra * 1.30
# Este método es para mostrar la información, pero aquí no hace nada, lo vamos a usar en las subclases.
    def mostrar_informacion(self):
        pass   # Será sobrescrito en las clases que heredan de esta.


class cuaderno(objetos):
    # Creamos un cuaderno que tiene precio, número de hojas y siempre es de la marca "HOJITAS".
    def __init__(self, precioCompra, hojas):
        super().__init__(precioCompra)
        self.hojas = hojas
        self.marca = "HOJITAS"

# Aquí mostramos toda la información del cuaderno: qué es, marca, hojas, precios.
    def mostrar_informacion(self):
        print(f"Artículo: Cuaderno")
        print(f"Marca: {self.marca}")
        print(f"Hojas: {self.hojas}")
        print(f"Precio de compra: ${self.precioCompra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")


class Lapiz(objetos):# Creamos un lápiz con precio y tipo (por ejemplo, grafito o colores) y la marca es "RAYAS".
    def __init__(self, precioCompra, tipo):
        super().__init__(precioCompra)
        self.tipo = tipo
        self.marca = "RAYAS" 

# Aquí mostramos la información del lápiz: qué es, marca, tipo y precios.
    def mostrar_informacion(self):
        print(f"Artículo: Lápiz")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precioCompra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")

# Creamos dos cuadernos con diferentes precios y número de hojas.
cuadernoA = cuaderno(precioCompra=1.50, hojas=50)
cuadernoB = cuaderno(precioCompra=2.80, hojas=100)

# Creamos dos lápices con diferentes precios y tipos (grafito y colores).
lapizA = Lapiz(precioCompra=0.30, tipo="Grafito")
lapizB = Lapiz(precioCompra=0.50, tipo="Colores")

# Mostramos la información de cada cuaderno y lápiz.
cuadernoA.mostrar_informacion()
print()
cuadernoB.mostrar_informacion()
print()
lapizA.mostrar_informacion()
print()
lapizB.mostrar_informacion()