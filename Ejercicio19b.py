#Visualice la cuenta de los múltiplos de 2 o de 3 que hay entre 1 y 100.
for i in range(1,101):
    if i%2==0 or i%3==0:
        print(i, end=" ")