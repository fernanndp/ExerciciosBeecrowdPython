s = 0
n = 1
i = 1
while i <= 39:
    s = float(s + (i/n))
    n = n * 2
    i+=2

print(f'{s:.2f}')