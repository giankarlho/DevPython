# Piedra:1, Papel:2, Tijera:3
jugador1 = int(input("Ing. la opción 1 o 2 o 3"))
jugador2 = 1 # La PC saca piedra

if jugador1 == 1 :
    print("Jugador1 saca 👊")
    if jugador2 == 1:
        print("Empataron los dos con 👊")
    if jugador2 == 2:
        print("Pierdo, jugador2 sacó 💌")
    if jugador2 == 3:
        print("Gano, jugador2 sacó ✂")
elif jugador1 == 2:
    print("Jugador1 saca 💌")
    if jugador2 == 1:
        print("Gano, jugador2 sacó 👊")
    if jugador2 == 2:
        print("Empataron los dos con 💌")
    if jugador2 == 3:
        print("Pierdo, jugador2 sacó ✂")
elif jugador1 == 3:
    print("Jugador1 saca ✂")
    if jugador2 == 1:
        print("Pierdo, jugador2 sacó 👊")
    if jugador2 == 2:
        print("Gano, jugador2 sacó 💌")
    if jugador2 == 3:
        print("Empatamos, los dos con ✂")
else:
     print("No haz elegido la opción correcta")   
       


