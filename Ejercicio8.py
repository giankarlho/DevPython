"""
  E8. Leer tres números distintos y nos diga
  cuál de ellos es el mayor.
"""
nro1 = int(input("Ing. el 1ero. nro"))
nro2 = int(input("Ing. el 2do. nro"))
nro3 = int(input("Ing. el 3ero. nro"))

if nro1 > nro2 and nro1 > nro3:
    print("El nro1 es mayor")
elif nro2 > nro1 and nro2 > nro3:
    print("El nro2 es mayor")
elif nro3 > nro1 and nro3 > nro2:
    print("El nro3 es mayor")
else:
    print("Los números son iguales")