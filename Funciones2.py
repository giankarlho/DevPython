import random
nro = random.randint(4,10)
print(nro)
def calPerfecto(nro): # Nro perfecto
    sd = 0
    for a in range(1,nro):
        if nro % a ==0:
            sd +=a  # cd = cd + a    
    if sd == nro:
        print("Es perfecto")
    else:
        print("No es perfecto")
    
def calPrimo(nro): # Nro primo
    cd = 0
    for a in range(1,nro+1):
        if nro % a ==0:
            cd +=1  # cd = cd + 1    
    if cd == 2:
        print("Es primo")
    else:
        print("No eres mi primo")

def calFactorial(nro): # Nro factorial
    prod=1
    for a in range(1,nro+1):
        prod = prod * a
    print(prod)
    
opcion = int(input("Que deseas calcular? 1: perfecto, 2: primo, 3: factorial"))
if opcion==1:
    calPerfecto(nro)
elif opcion ==2:
    calPrimo(nro)
elif opcion == 3:
    calFactorial(nro)
else:
    print("Ingresa 1 o 2 o 3, porfavor")
