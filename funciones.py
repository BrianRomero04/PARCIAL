"""""
def mifuncion():
    print("Programacion III")

mifuncion()

def par(num):
    residuo = num%2
    if(residuo==0):
        print("es par")
    else:
        print("es impar")
par(5)



funcion bool()
La función bool() en Python es una función incorporada que se utiliza para evaluar el valor de verdad 
(verdadero o falso) de una expresión o un objeto. Esta función toma un único argumento y devuelve True
si el argumento es evaluado como verdadero, y False si el argumento es evaluado como falso.

bool(0)         # Devuelve False
bool(42)        # Devuelve True
bool(-3.14)     # Devuelve True
"""
#1 area de un circulo
import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Ejemplo de uso
radio = 5
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es {area}")

#2
def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

# Ejemplo de uso
diagonal_mayor = 10
diagonal_menor = 6
area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
print(f"El área del rombo con diagonales {diagonal_mayor} y {diagonal_menor} es {area}")

#3
def calcular_distancia(velocidad, tiempo):
    distancia = velocidad * tiempo
    return distancia

# Ejemplo de uso
velocidad = 60  # en metros por segundo (m/s)
tiempo = 120  # en segundos (s)
distancia = calcular_distancia(velocidad, tiempo)
print(f"La distancia recorrida con una velocidad de {velocidad} m/s durante {tiempo} segundos es {distancia} metros")
