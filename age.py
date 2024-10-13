contador = 0
soma = 0
while(True):
    x = int(input())
    if(x > 0):
        contador+=1
        soma+=x
    if(x < 0):
        break
media = soma/contador
print(f'{media:.2f}')

