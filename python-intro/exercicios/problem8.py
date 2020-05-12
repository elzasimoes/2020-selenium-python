dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')

if mes == '1':
    print(f'Você nasceu no dia {dia}, de janeiro do ano de {ano}')
elif mes == '2':
    print(f'Você nasceu no dia {dia}, de feveiro do ano de {ano}')
elif mes == '3':
    print(f'Você nasceu no dia {dia}, de março do ano de {ano}')
elif mes == '4':
    print(f'Você nasceu no dia {dia}, de abril do ano de {ano}')
elif mes == '5':
    print(f'Você nasceu no dia {dia}, de meio do ano de {ano}')
elif mes == '6':
    print(f'Você nasceu no dia {dia}, de junho do ano de {ano}')
elif mes == '7':
    print(f'Você nasceu no dia {dia}, de julho do ano de {ano}')
elif mes == '8':
    print(f'Você nasceu no dia {dia}, de agosto do ano de {ano}')
elif mes == '9':
    print(f'Você nasceu no dia {dia}, de setembro do ano de {ano}')
elif mes == '10':
    print(f'Você nasceu no dia {dia}, de outubro do ano de {ano}')
elif mes == '11':
    print(f'Você nasceu no dia {dia}, de novembro do ano de {ano}')
elif mes == '12':
    print(f'Você nasceu no dia {dia}, de dezembro do ano de {ano}')


resposta = input('Qual sua data de nascimento?  ')
# 06/03/1993

dia, mes, ano = resposta.split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}')
