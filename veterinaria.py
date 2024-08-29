
class Perros:
    # Aquí se crea un "Perro" con sus características: raza, nombre, peso, edad, nombre y correo del dueño.
    def __init__ (self, raza, nombre, peso, edad, nombre_dueño, correo_dueño):
        self.raza = raza
        self.nombre = nombre
        self.peso = peso
        self.edad = edad
        self.nombre_dueño = nombre_dueño
        self.correo_dueño = correo_dueño
        self.estado = "NO ATENDIDO"# El perro empieza sin haber sido atendido.
        self.tamaño = self.definir_tamaño()# Se decide si el perro es grande o pequeño según su peso.

 # Esta parte decide si el perro es pequeño o grande.
    def definir_tamaño(self):
            if self.peso < 10:
                return "perro pequeño"# Si pesa menos de 10 kg, es pequeño.
            else:
                return "perro grande"# Si pesa 10 kg o más, es grande.
            
  # Aquí marcamos al perro como "ATENDIDO" después de que lo hayan revisado.
    def registrarAtencion(self):
            self.estado = "ATENDIDO"
  # Esta parte muestra toda la información del perro y su dueño.
    def mostrar_informacion(self):
            print(f"raza: {self.raza}")
            print(f"nombre: {self.nombre}")
            print(f"peso: {self.peso} kg")
            print(f"edad: {self.edad} años")
            print(f"dueño: {self.nombre_dueño}")
            print(f"correo del Dueño: {self.correo_dueño}")
            print(f"estado: {self.estado}")
            print(f"tamaño: {self.tamaño}")

# Aquí es donde pedimos los datos del perro y su dueño para crear un "Perro" con toda esa información.
nombre = input("Ingrese la raza del perro: ")
raza = input("Ingrese el nombre del perro: ")
edad = int(input("Ingrese el peso del perro (en kg): "))
peso = float(input("Ingrese la edad del perro "))
dueño = input("Ingrese el nombre del dueño: ")
correo_dueño = input("Ingrese el correo del dueño: ")

# Creamos un nuevo perro con la información que dimos y lo marcamos como "ATENDIDO".
perro = Perros(raza, nombre, peso, edad, dueño, correo_dueño)
perro.registrarAtencion()
perro.mostrar_informacion()
