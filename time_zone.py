S,T,F = map(int, input().split(' '))
if(S==0):
    S=24
horario = S+T+F
if(horario>24):
    horario = horario-24
    print(f'{horario}')
elif(horario == 24):
    horario = 0
    print(f'{horario}')
else:
    print(f'{horario}')
