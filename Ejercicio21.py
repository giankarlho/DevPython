# Determinar si un alumno aprueba o desaprueba una materia, 
# basado en promedio de N calificaciones.
import random
suma = 0
cantCal = random.randint(3,5) # generar la cant. de calificaciones
for i in range (cantCal):
    notas = random.randint(0,20) # generar las notas aleatorias del 0 - 20    
    print(notas)
    suma += notas
print("Su promedio de notas es:",suma//cantCal)    
