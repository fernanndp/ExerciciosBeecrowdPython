linha = input().split(' ')
c1 = int(linha[0])
n1 = int(linha[1])
p1 = float(linha[2])

linha2 = input().split(' ')
c2 = int(linha2[0])
n2 = int(linha2[1])
p2 = float(linha2[2])

total1 = n1*p1
total2 = n2*p2

total = total1+total2
print(f'VALOR A PAGAR: R$ {total:.2f}')