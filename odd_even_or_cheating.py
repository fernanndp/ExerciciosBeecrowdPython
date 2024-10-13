p, j1, j2, r, a = map(int, input().split(' '))
resultado = (j1 + j2)%2 
if(r == 0 and a == 1):
    print('Jogador 1 ganha!')
elif(r == 1 and a == 1):
    print('Jogador 2 ganha!')
elif(r == 1 and a == 0):
    print('Jogador 1 ganha!')
else:
    if(resultado == 0 and p == 1):
        print('Jogador 1 ganha!')
    elif(resultado == 0 and p == 0):
        print('Jogador 2 ganha!')
    elif(resultado != 0 and p == 0):
        print('Jogador 1 ganha!')    
    elif(resultado != 0 and p == 1):
        print('Jogador 2 ganha!')