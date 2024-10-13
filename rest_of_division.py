x = int(input())
y = int(input())
if(x > y):
   aux = x
   x = y
   y = aux 
while(x<y):
   x += 1
   if((x%5 == 2) or (x%5 == 3) and x!=y):
      print(x)