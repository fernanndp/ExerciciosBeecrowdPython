N = int(input())
C = 0
R = 0
S = 0
for i in range(N):
    a,animal = map(str, input().split())
    a = int(a)
    if(animal == 'C'):
        C += a
    elif(animal == 'R'):
        R += a
    else:
        S += a
total = C + R + S
cp = C*100/total
rp = R*100/total
sp = S*100/total
print(f'Total: {total} cobaias')
print('Total de coelhos:', C)
print('Total de ratos:', R)
print('Total de sapos:', S)
print(f'Percentual de coelhos: {cp:.2f} %')
print(f'Percentual de ratos: {rp:.2f} %')
print(f'Percentual de sapos: {sp:.2f} %')
