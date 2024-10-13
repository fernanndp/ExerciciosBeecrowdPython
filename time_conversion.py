segundos = int(input())
minutos = int(segundos/60)

segundos %= 60
horas =  int(minutos/60)
minutos %= 60

print(f'{horas}:{minutos}:{segundos}')