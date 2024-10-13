N=int(input())
a=0
b=1
print(a,end=" ")
print(b,end=" ")
i=2
while(True):
    c=a+b
    i+=1
    if(i==N):
        print(c)
        break
    else:
        print(c,end=" ")
        a=b
        b=c