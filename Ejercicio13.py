nro=int(input('Ing, un numero'))
a=nro//10
b=nro%10
if(a%b==0 or b%a ==0):
    print('Son múltiplos')
else:
    print('No son multiplos')