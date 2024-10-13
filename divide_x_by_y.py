N = int(input())
i = 0
while(i<N):
    X, Y = map(int, input().split(' '))
    if(Y == 0):
        print('divisao impossivel')
    else:
        print(f'{(X/Y):0.1f}')
    i+=1