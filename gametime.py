Hi, Hf = map(int, input().split(' '))
if(Hi<Hf):
    tempo = Hf - Hi
else:
    tempo = Hf + 24 - Hi
print(f'O JOGO DUROU {tempo} HORA(S)')