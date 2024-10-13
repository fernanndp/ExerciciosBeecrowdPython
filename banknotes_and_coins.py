N = float(input())
centavos = N*100
N100 = (centavos//10000)
centavos = centavos%10000
N50 = (centavos//5000)
centavos = centavos%5000
N20 = (centavos//2000)
centavos = centavos%2000
N10 = (centavos//1000)
centavos = centavos%1000
N5 = (centavos//500)
centavos = centavos%500
N2 = (centavos//200)
centavos = centavos%200
M1 = (centavos//100)
centavos = centavos%100
M50 = (centavos//50)
centavos = centavos%50
M25 = (centavos//25)
centavos = centavos%25
M10 = (centavos//10)
centavos = centavos%10
M5 = (centavos//5)
centavos = centavos%5
M01 = centavos//1
print("NOTAS:")
print(f"{int(N100)} nota(s) de R$ 100.00")
print(f"{int(N50)} nota(s) de R$ 50.00")
print(f"{int(N20)} nota(s) de R$ 20.00")
print(f"{int(N10)} nota(s) de R$ 10.00")
print(f"{int(N5)} nota(s) de R$ 5.00")
print(f"{int(N2)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(M1)} moeda(s) de R$ 1.00")
print(f"{int(M50)} moeda(s) de R$ 0.50")
print(f"{int(M25)} moeda(s) de R$ 0.25")
print(f"{int(M10)} moeda(s) de R$ 0.10")
print(f"{int(M5)} moeda(s) de R$ 0.05")
print(f"{int(M01)} moeda(s) de R$ 0.01")