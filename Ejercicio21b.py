import random

datos=[]
suma=0
nota=0
cantidad_notas=random.randint(1,10)
for i in range(1,cantidad_notas):
    k=random.randint(0,20)
    suma+=k
    datos.append(k)
nota=suma/len(datos)
if int(nota)>=14:
    print(f"Aprueba con {nota}")
else:
    print(f"desaprueba con {nota}")

