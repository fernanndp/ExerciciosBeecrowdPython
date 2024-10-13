a, b, c = map(int, input().split(' '))
if(a>b):
    if(b<c or b==c):
        print(":)")
    else:
        if((b-c) < (a-b)):
            print(":)")
        elif((b-c)>=(a-b)):
            print(":(")          
elif(a<b):
    if(b>c or b==c):
        print(":(")
    else:
        if((c-b) < (b-a)):
            print(":(")
        elif((c-b)>=(b-a)):
             print(":)")
         
else:
    if(b<c):
        print(":)")
    elif(b>c):
        print(":(")

