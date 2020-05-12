produto1 = float(input('Qual o valor do primeiro produto: '))
produto2 = float(input('Qual o valor do segundo produto: '))
produto3 = float(input('Qual o valor do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
    print(f'O mais barato é o primeiro produto, no valor de R${produto1} reais')
elif produto2 < produto1 and produto2 < produto3:
    print(f'O mais barato é o segundo produto, no valor de R${produto2} reais')
elif produto3 < produto1 and produto3 < produto2:
    print(f'O mais barato é o terceiro produto, no valor de R${produto3} reais')
