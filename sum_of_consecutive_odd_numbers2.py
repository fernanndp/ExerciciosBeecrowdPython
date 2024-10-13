N = int(input())

for i in range(N):
    x, y = map(int,input().split())
    o = 0
    if(x == y):
        print(0)
    else:
        aux = 0 
        if(x>y):
            aux = x
            x = y
            y = aux
        while(x<y-1):
            x += 1
            if(x%2 != 0):
                o += x
        print(o)