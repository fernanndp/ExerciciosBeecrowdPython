a, b, c, d = map(float,input().split(' '))
media = (a * 2 + b * 3 + c * 4 + d * 1)/10
print(f'Media: {media:.1f}')
if (media >= 7.0):
    print("Aluno aprovado.")
elif(media < 5.0):
    print("Aluno reprovado.")
elif(media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")
    n = float(input())
    print(f"Nota do exame: {n:.1f}")
    mediafinal = (media + n)/2
    if(mediafinal >= 5.0):
        print("Aluno aprovado.")
        print(f'Media final: {mediafinal:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {mediafinal:.1f}')