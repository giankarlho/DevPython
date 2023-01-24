# Piedra:1, Papel:2, Tijera:3
jugador1 = int(input("Ing. la opción 1 o 2 o 3"))
jugador2 = 1 # La PC saca piedra
if jugador1 == jugador2 :
    print("Empataron")
else:
    if (jugador1 == 1 and jugador2 == 2) or (jugador1 == 2 and jugador2 == 3) or (jugador1 == 3 and jugador2 == 1):
        print("Pierde el jugador1")                
    elif (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 ==3 and jugador2 == 2):
        print("Gana el jugador1)
    else:
        print("No haz elegido la opción correcta")