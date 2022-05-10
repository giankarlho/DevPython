#Visualice la cuenta de los múltiplos de 2 o de 3 que hay entre 1 y 100.
count = 1
valores = []
while count <=100 :
    if  count % 2 == 0 or count % 3 == 0: 
        valores.append(count)
    count = count + 1 
print("los siguientes valores son multiplo de 2 o 3:",valores)
