#Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))
n4 = int(input('Numero 4: '))
n5 = int(input('Numero 5: '))

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print('Numero 1 é o maior.')
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print('Numero 2 é o maior.')
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print('Numero 3 é o maior.')
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print('Numero 4 é o maior.')
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print('Numero 5 é o maior.') 
