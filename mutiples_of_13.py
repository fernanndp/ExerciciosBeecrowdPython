a = int(input())
b = int(input())
if(b<a):
    aux = b
    b = a
    a = aux
soma = 0
for i in range(a,b+1):
    if(i%13 != 0):
        soma+=i
print(soma)