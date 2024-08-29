#Este programa ayuda a un equipo pequeño a mantenerse organizado al permitir un fácil seguimiento 
# de quién está trabajando en qué tarea y cuál es su estado.


class Tarea:
    def __init__(self, nombre, responsable):
        # Inicializa una nueva tarea con nombre, responsable y estado de completada.
        self.nombre = nombre
        self.responsable = responsable
        self.completada = False

    def completar_tarea(self):
        # Marca la tarea como completada.
        self.completada = True

    def mostrar_informacion(self):
        # Muestra la información de la tarea, incluyendo su estado.
        estado = "Completada" if self.completada else "Pendiente"
        print(f"Tarea: {self.nombre} | Responsable: {self.responsable} | Estado: {estado}")


tareas = []  # Lista para almacenar todas las tareas.

# Ciclo para agregar nuevas tareas
while True:
    nombre_tarea = input("Ingrese el nombre de la tarea: ")
    responsable_tarea = input("Ingrese el responsable de la tarea: ")
    
    # Crea una nueva tarea con los datos proporcionados.
    tarea = Tarea(nombre_tarea, responsable_tarea)
    # Agrega la tarea a la lista de tareas.
    tareas.append(tarea)

    # Pregunta al usuario si desea agregar otra tarea.
    continuar = input("¿Desea agregar otra tarea? (s/n): ")
    if continuar.lower() != 's':
        break

# Ciclo para actualizar el estado de las tareas
while True:
    # Muestra todas las tareas actuales.
    print("\nLista de tareas:")
    for tarea in tareas:
        tarea.mostrar_informacion()
    
    # Permite al usuario marcar una tarea como completada.
    nombre_completar = input("\nIngrese el nombre de la tarea que desea marcar como completada: ")
    for tarea in tareas:
        if tarea.nombre == nombre_completar:
            tarea.completar_tarea()
            print(f"Tarea '{tarea.nombre}' marcada como completada.")
            break
    else:
        print("La tarea especificada no se encontró.")

    # Pregunta al usuario si desea marcar otra tarea como completada o cerrar el ciclo.
    continuar = input("¿Desea marcar otra tarea como completada? (s/n): ")
    if continuar.lower() != 's':
        break

# Muestra el estado actualizado de todas las tareas.
print("\nEstado actualizado de las tareas:")
for tarea in tareas:
    tarea.mostrar_informacion()
