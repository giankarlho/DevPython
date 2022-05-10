# visualizar los múltiplos de 2 o 3 hasta el 100
for i in range(1,101):
    if (i%2==0 or i%3==0):
        print(i,"\t", end=" ") 
print()
# visualizar los múltiplos de 2 y 3 hasta el 100
for i in range(1,101):
    if (i%6==0):
        print(i,"\t", end=" ")     