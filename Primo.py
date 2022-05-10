# Nro primo: 7: 1,7
import random
nro = random.randint(4,120)
print(nro)
cd = 0
for a in range(1,nro+1):
    if nro % a ==0:
        cd +=1  # cd = cd + 1    
if cd == 2:
    print("Es primo")
else:
    print("No eres mi primo")