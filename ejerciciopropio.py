class Tarea:
    def __init__(self, nombre, responsable):
        # Cuando creamos una tarea, le damos un nombre y una persona responsable.
        # Por defecto, la tarea no está completada (completada = False).
        self.nombre = nombre
        self.responsable = responsable
        self.completada = False

# Este método marca la tarea como completada.
    def completar_tarea(self):
        self.completada = True

# Aquí mostramos la información de la tarea, el nombre de la tarea, la persona responsable y si está completada o pendiente.
    def mostrar_informacion(self):
        estado = "Completada" if self.completada else "Pendiente"
        print(f"Tarea: {self.nombre} | Responsable: {self.responsable} | Estado: {estado}")


tareas = []# Aquí guardaremos todas las tareas.

while True:
    # Pedimos al usuario el nombre y el responsable de la tarea.
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    responsable_tarea = input("Ingrese el responsable de la tarea: ")
    
    # Creamos una nueva tarea con los datos proporcionados.
    tarea = Tarea(nombre_tarea, responsable_tarea)
    tareas.append(tarea)

 # Preguntamos al usuario si quiere agregar otra tarea, si el usuario responde que no, salimos del bucle.
    continuar = input("¿Desea agregar otra tarea? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostramos todas las tareas que hemos agregado.
print("\nLista de tareas:")
for tarea in tareas:
    tarea.mostrar_informacion()

# Actualizamos el estado de una tarea a completada, marcamos la tarea especificada como completada.
nombre_completar = input("\nIngrese el nombre de la tarea que desea marcar como completada: ")
for tarea in tareas:
    if tarea.nombre == nombre_completar:
        tarea.completar_tarea()
        print(f"Tarea '{tarea.nombre}' marcada como completada.")

# Mostramos el estado actualizado de todas las tareas.
print("\nEstado actualizado de las tareas:")
for tarea in tareas:
    tarea.mostrar_informacion()
