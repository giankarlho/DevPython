num=int(input('digite un numero'))
max,min,suma,contador=num,num,0,0
while num!=0:
    print(num)
    if num>max:
        max=num
    if num<min:
        min=num     
    suma+=num
    contador+=1
    num=int(input('digite un numero'))
print('minimo',min)
print('maximo',max)
print('promedio',suma//contador)

    