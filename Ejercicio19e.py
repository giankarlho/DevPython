#Lee números enteros hasta teclear 0, y nos muestra el máximo, 
#el mínimo y la media de todos ellos. Piensa cómo debemos inicializar las variables.
nroMax,nroMin =0,10000
cant,suma = 0,0
while True:
    nro=int(input("Ingrese un nro menos que 5 cifras"))
    if (nro == 0):         
        break
    cant +=1    # count = count + 1   |  contador
    suma +=nro    # sum = sum + nro     |  acumulador    
    if (nro > nroMax):
        nroMax = nro     
    if (nro < nroMin):
        nroMin = nro       
print ("El nro mayor es:",nroMax)
print ("El nro menor es:",nroMin)
print ("El nro prom es:",suma/cant)
