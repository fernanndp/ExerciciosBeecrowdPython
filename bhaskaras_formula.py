import math
A, B, C = map(float, input().split())
D = (B**2) - (4*A*C)
if (D < 0 or A == 0):
    print("Impossivel calcular")
else:
    D = math.sqrt(D)
    R1 = (-B + D)/(2*A)
    R2 = (-B - D)/(2*A)
    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5F}')

