# 48 .Encontrar el mayor y menor valor de una lista entera aleatoria de N elementos de dos cifras.
import random
lista = []
cantidadElement = random.randint(10,20)
for i in range(1, cantidadElement + 1):
    lista.append(random.randrange(10))  # ingresa un valor en la última posición
lista.sort()        # Ordenando la lista de forma ascendente
print("El mayor de la lista es :", lista[-1])
print("El menor de la lista es :", lista[0])