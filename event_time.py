dia, d1 = input().split()
d1 = int(d1)
h1, m1, s1 = map(int, input().split(':'))

dia2, d2 = input().split()
d2 = int(d2)
h2, m2, s2 = map(int, input().split(':'))

d = d2 - d1
h = h2 - h1 
m = m2 - m1
s = s2 - s1

if(s<0):
    s += 60
    m -= 1
if(m<0):
    m += 60
    h -= 1
if(h<0):
    h+=24
    d-=1
print(f'{d} dia(s)')
print(f'{h} hora(s)')
print(f'{m} minuto(s)')
print(f'{s} segundo(s)')