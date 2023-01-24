# 48 .Encontrar el mayor y menor valor de una lista entera aleatoria de N elementos de dos cifras.
import random
lista = []
nroMayor,nroMenor = -1,999
cantidadElement = random.randint(10,20)
for i in range(1, cantidadElement + 1):
    lista.append(random.randrange(10))  # ingresa un valor en la última posición
    if lista[-1] < nroMenor:
        nroMenor = lista[-1]
    if lista[-1] > nroMayor:
        nroMayor = lista[-1]   
print("el nro. mayor es:" , nroMayor)
print("el nro. menor es:" , nroMenor)


