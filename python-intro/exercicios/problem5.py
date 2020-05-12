###################

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

if media >= 7 and media < 10:
    print('Parabens você foi aprovado')
elif media == 10:
    print('Parabéns, vc atingiu a nota máxima')
else:
    print('Oops, você foi reprovado')
