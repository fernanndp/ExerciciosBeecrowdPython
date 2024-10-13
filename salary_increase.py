salario = float(input())
if(salario>=0 and salario<=400):
    perc = 0.15
elif(salario>400 and salario<=800):
    perc = 0.12
elif(salario>800 and salario<=1200):
    perc = 0.1
elif(salario > 1200 and salario <=2000):
    perc = 0.07
else:
    perc = 0.04
reajuste = salario*perc
novoSalario = salario + reajuste
print(f'Novo salario: {novoSalario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {int(perc*100):.2f}')