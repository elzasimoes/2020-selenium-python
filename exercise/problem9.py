
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
#válido.

nota = -1

while nota < 0 or nota > 10:
    nota = int(input("Informe a sua nota de 0 á 10: "))
    if nota > 0 or nota < 10:
        print('Valor correto. :)')
    if nota < 0 or nota > 10:
        print("Valor inválido, digite novamente: ")
