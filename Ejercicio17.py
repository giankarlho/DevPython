nro=int(input("Ing. un nro. mayor a 0"))
tope = nro
if nro%2 !=0: # si es inpar
    nro = nro +1    
valores=nro-2
suma = 0
for i in range(1,tope+1):
    valores = valores + 2
    suma = suma + valores    
    print(valores,"\t",end="")
print('La suma es',suma)



