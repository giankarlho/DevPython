def suma(a,b):
    return (a + b)

def resta(a,b):
    return (a -b)

def calcularBisiesto(age):	
    if age%4 == 0 and age % 100 != 0:
        print('El año',age,'Es bisiesto')
    elif age%100 == 0 and age%400 == 0:
        print('El año',age,'Es bisiesto')
    else:
        print('El año',age,'No es bisiesto')
        
nro1 = int(input("Ing. el nro. 1"))
operador=input("Ing operador: +,-")
nro2 = int(input("Ing. el nro. 2"))
resul = 0
if operador=='+':
    resul = suma(nro1,nro2)
elif operador=='-':
    resul = resta(nro1,nro2)

if (resul >100):
    calcularBisiesto(2021)
else:
    calcularBisiesto(2000)
    
print("El resultado",resul)