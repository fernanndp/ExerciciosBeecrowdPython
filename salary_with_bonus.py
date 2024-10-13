nome = input()
salarioFixo = float(input())
vendasTotais = float(input())

bonus = float(vendasTotais * (15/100))
salarioTotal = salarioFixo + bonus


print(f'TOTAL = R$ {salarioTotal:.2f}') 