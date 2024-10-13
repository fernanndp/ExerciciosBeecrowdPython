A,B,C = map(float, input().split(' '))
tri = A * C * 0.5
cir = (C**2) * 3.14159
tra = (A+B)/C*2
sqr = B**2
ret = A*B
print(f"TRIANGULO = {tri:.3f}\nCIRCULO = {cir:.3f}\nTRAPEZIO = {tra:.3f}\nQUADRADO = {sqr:.3f}\nRETANGULO = {ret:.3f}")