# Dado un año, nos diga si es bisiesto o no. Es bisiesto bajo lo siguiente condición:
# Un año divisible por 4 y no debe ser divisible entre 100.
# Si un año es divisible entre 100 y además es divisible entre 400.
year = int(input("Ingrese el numero"))
if (year % 4 == 0 and year % 100 !=0):
    print(year, "Es año bisiesto")
elif (year % 100 == 0 and year % 400 == 0 or year % 4 == 0):
    print(year, "Es año bisiesto")
elif (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print(year, "Es año bisiesto")
else:
    print(year, "No es año bisiesto")