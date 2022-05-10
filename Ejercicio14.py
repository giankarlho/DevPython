nro=int(input("ingresa un numero de dos digitos: "))
a=nro//10
b=nro%10
if a%b==0 or b%a==0:
    print("son multiplos")
else:
    print("no son multiplos")




