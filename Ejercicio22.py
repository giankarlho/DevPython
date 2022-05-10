

nombre=input("Ingrese el Nombre del Alumno : ")

Pra=float(input("Nota de Practica : "))
Pro=float(input("Nota de Problemas : "))
Te=float(input("Nota de Teoria : "))

if 0<=Pra<=20 and 0<=Pro<=20 and 0<=Te<=20 :

    Pra_porcentaje=(Pra*10)/20
    Pro_porcentaje=(Pro*50)/20
    Te_porcentaje=(Te*40)/20 

    total_porcentaje=Pra_porcentaje+Pro_porcentaje+Te_porcentaje

    total_numeros=(20*total_porcentaje)/100

    print(f" la nota del alumno {nombre} es {total_numeros}")


    
else:
    print("error ingrese una nota valida")
