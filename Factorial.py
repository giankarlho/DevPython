# Factorial
# 5! = 1x2x3x4x5
# 8! = 1x2x3x4x5x6x7x8
import random
nro = random.randint(4,10)
prod=1
for a in range(1,nro+1):
    prod = prod * a
print(prod)