# Simular el lanzamiento de dos dados y sumar los resultados. 
# El juego terminará cuando haya dos sumas consecutivas iguales.
import random
sumaAnterior = 0
while True:
    suma=random.randint(1,6) + random.randint(1,6)    
    if suma != sumaAnterior:
        sumaAnterior = suma        
    else:
        print("Salió por la condición ",suma,sumaAnterior)
        break





