import math
A, B, C = map(int,input().split(' '))
maior = (A + B + abs(A-B))/2
result = (int(maior) + C + abs(int(maior)-C))/2
print(f'{int(result)} eh o maior')