# Ejercicio 3
# Lee dos números
# imprime cuál de ellos es mayor o bien si son iguales. 
nro1 = int(input("Ing. el 1er. nro.: "))
nro2 = int(input("Ing. el 2do. nro.: "))
#print(type(nro1), type(nro2))
if (nro1 > nro2):
    print("El nro1. es mayor")
elif (nro2 > nro1):
    print("El nro2. es mayor")
else:
    print("Los dos nros. son Iguales")
print("Nro1:", nro1, ", Nro.2:", nro2)
    