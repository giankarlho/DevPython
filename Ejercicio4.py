# Ejercicio 4
# Diseñar un algoritmo que pida por teclado tres números;
# si el primero es negativo, debe imprimir el producto de los tres 
# y si no lo es, imprimirá la suma.
nro1 = int(input("Ing. el 1er. nro.: "))
nro2 = int(input("Ing. el 2do. nro.: "))
nro3 = int(input("Ing. el 3er. nro.: "))
if (nro1 < 0):
    print("El producto es: ", nro1*nro2*nro3)
else:
    print("La suma es: ", (nro1+nro2+nro3))
