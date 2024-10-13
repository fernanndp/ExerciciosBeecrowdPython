Hi, Mi, Hf, Mf = map(int, input().split())
MiT = Mi + Hi*60
MfT = Mf + Hf*60

if(MfT>MiT):
    d = MfT - MiT
else: 
    d = (24*60) + MfT - MiT
DH = d//60
DM = d%60
print(f'O JOGO DUROU {DH} HORA(S) E {DM} MINUTO(S)')