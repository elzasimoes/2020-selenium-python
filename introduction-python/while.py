"resposta = input('Vamos sair hoje [s/n]??')
n = 1

while  resposta != 's':
    resposta = input(f'Bora{"a" * n}??')
    n += 1
    if 'chato' in resposta or 'chata' in resposta:
        print('Foi mal')
        break
    elif 's' in resposta:
        print('Então bora')
