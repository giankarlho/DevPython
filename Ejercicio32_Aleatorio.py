""" Calcule la suma y promedio de los N números ingresados por
 teclado hasta que se ingrese un número negativo."""
import random
suma,cantidad,promedio = 0,0,0
while True:
    nro = random.randrange(-10,100)
    if nro < 0:
        break
    suma = suma + nro
    cantidad = cantidad + 1
promedio = suma // cantidad
print("El promedio es: ", promedio)

