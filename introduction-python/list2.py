lista_de_compras = []
resposta = ''

while resposta != 'acabou':
    resposta = input('Inserir na lista de compras: ')
    if resposta != 'acabou':
        lista_de_compras.append(resposta)


    print(lista_de_compras)
