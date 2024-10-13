while(True):
    i = 0
    media = 0
    while(i<2):
        x = float(input())
        if (x < 0 or x > 10):
            print('nota invalida')
        else:
            i+=1
            media += x
    media = media/2
    print(f'media = {media:.2f}')
    y = 0
    while(True):
        print('novo calculo (1-sim 2-nao)')
        y = int(input())
        if(y == 1 or y == 2):
            break
    if(y == 2):
        break
    