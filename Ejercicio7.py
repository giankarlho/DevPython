'''
Una tienda hace un descuento de $10 si el total de compra
es mayor a $500. 
Deberás calcular el precio a pagar, basado en el valor 
de la compra.
'''
totalCompra = float(input("Ing. el total"))
if totalCompra > 500:
    print("El total a pagar es: ", (totalCompra -10))
else:
    print("El total a pagar es: ", totalCompra)
