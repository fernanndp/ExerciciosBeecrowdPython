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
print(f'media = {media}')
    
