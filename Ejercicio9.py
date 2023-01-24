"""
Una tienda hace:
- Dscto. de $10 si $100 >= el total la compra < $200,
- Dscto. de $20 si el total de la compra > 200.
- Si la compra es menor de $100, S/0 dscto.
El algoritmo debe calcular el 
precio a pagar, basado en el valor de la compra.
"""
totalCompra = float(input("Ing. el Total de compra"))
if totalCompra >=100 and totalCompra <200:
    print("El importe es: ", (totalCompra - 10))
elif totalCompra >200:
    print("El importe es: ", (totalCompra - 20))
else:
    print("El importe es: ", totalCompra)