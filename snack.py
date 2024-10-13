X, Y = map(int, input().split(' '))
if(X == 1):
    total = (float)(4.00 * Y)
elif(X == 2):
    total = (float)(4.50 * Y)
elif(X == 3):
    total = (float)(5.00 * Y)
elif(X == 4):
    total = (float)(2.00 * Y) 
elif(X == 5):
    total = (float)(1.50 * Y)
print(f'Total: R$ {total:.2f}')


