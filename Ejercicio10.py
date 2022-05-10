#Una tienda hace un descuento de $10 si el total de la compra está
#entre $100 y $200, y hace un descuento de $20 si el total de la
#compra es mayor de $200. Si la compra es menor de $100, no hay 
#descuento. El algoritmo debe calcular el precio a pagar, basado 
#en el valor de la compra.

compra = float(input("Ingrese el total de la compra"))
if compra >=100 and compra <=200:
       print("Total a pagar es:",compra-10)
if compra > 200:
    print("Total a pagar es:",compra-20)
elif compra <=100:
    print("Total a pagar es:",compra)

