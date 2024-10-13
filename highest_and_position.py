maior = 0
posic = 0
for i in range(100):
    n = int(input())
    if (n>maior):
        maior = n
        posic = i
print(maior)
print(posic+1)