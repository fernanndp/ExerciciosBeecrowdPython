while(True):
    M, N = map(int, input().split(' '))
    if(M>N):
            aux = M
            M = N
            N = aux

    if(M <= 0 or N <= 0):
        break

    else:
        soma = 0
        for i in range(M,N+1):
            print(f'{i}', end=' ')
            soma += i
        print(f'Sum={soma}')