a, n = map(int, input().split(' '))
soma = 0
if(n<=0):
    n = int(input())
else:
    for i in range(0, n):
        soma += a + i
    print(soma)