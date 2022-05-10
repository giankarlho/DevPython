import random
cantRound = int(random.randint(1,10))
monto = 2**(cantRound-1)*50
if cantRound ==10:
    monto = monto + 200
print('El monto a pagar ', monto, " sobrevivió el ", cantRound, " round")