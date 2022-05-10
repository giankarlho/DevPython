# Nro. perfecto: 6 = 1 + 2 + 3
import random
nro = random.randint(4,10)
print(nro)
sd = 0
for a in range(1,nro):
    if nro % a ==0:
        sd +=a  # cd = cd + a    
if sd == nro:
    print("Es perfecto")
else:
    print("No es perfecto")
    