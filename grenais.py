inter = 0
gremio = 0
empates = 0
grenais = 0
while True:
    a,b = list(map(int,input().split()))
    if(a>b):
        inter=inter+1
    if(a<b):
        gremio=gremio+1
    if(a==b):
        empates=empates+1
    grenais+=1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if(n==1):
        continue
    if(n==2):
        break
print("{} grenais".format(grenais))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empates))
if(inter>gremio):
    print("Inter venceu mais")
if(inter<gremio):
    print("Gremio venceu mais")
if(inter==gremio):
    print("Nao houve vencedor")