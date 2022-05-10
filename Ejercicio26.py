k=int(input("Ingrese un numero : "))
primos=[]
suma=0
n=0

for i in range(1,k+1):

    for j in range(i+1):

        if j!=0:
            if i%j==0 and j!=0:
                n+=1
    if n<=2:

        suma+=i
        primos.append(i)
    n=0

print(primos)
print(suma)


