# Dado un tiempo en minutos, calcula los días, las horas y minutos que corresponde.
tiempo = int(input("Ing. la cantidad de minutos : "))
if (tiempo > 1440 or tiempo > 3600):
    print(f"Según el tiempo los dias son : {tiempo // 1440}")
    print(f"Según el tiempo las horas son : {tiempo // 360}")
    print(f"Según el tiempo los minutos son : {tiempo}")