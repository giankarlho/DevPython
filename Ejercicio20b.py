# Determinar si un alumno aprueba o desaprueba una materia, 
# basado en promedio de N calificaciones.

suma = 0
cantCal = int(input("Ing. la cant. de criterios de calificación"))
for i in range (cantCal):
    notas = int(input("Ing. la nota"))
    print(notas)
    suma += notas
prom =suma//cantCal
print("Su promedio de notas es:",prom)    
if (prom > 12):
    print("Aprobado")
else:
    print("Desaprobado")

# con random          
import random
suma = 0
cantCal = random.randint(3,5) # generar la cant. de calificaciones
for i in range (cantCal):
    notas = random.randint(0,20) # generar las notas aleatorias del 0 - 20    
    print(notas)
    suma += notas       # suma = suma + notas   
prom = suma//cantCal
print("Su promedio de notas es:",prom)    
if (prom > 12):
    print("Aprobado")
else:
    print("Desaprobado")