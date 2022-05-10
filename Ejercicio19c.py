datos=[]
suma=0
while True:
    n=int(input("Ingrese un numero : "))
    if n == 0:
        break
    datos.append(n)
datos.sort()
for i in datos:
    suma+=i
print(f"El maximo es {datos[-1]}") 
print(f"El minimo es {datos[0]}")
print(f"La media es {suma/len(datos)}")

