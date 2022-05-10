#altura=int(input("Ingrese la Altura : "))

import random
altura = random.randint(4,100) 
n=altura
for i in range(altura,0,-1):
    n-=1
    print(" "*(altura-n),i*"*","\t"*1,i*"*")
