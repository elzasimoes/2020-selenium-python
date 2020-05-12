minha_lista_de_compras = ['Sabão', 'Sabonete', 'Arroz', 'Feijão', 10, [1, 2, 3]]

for coisa in minha_lista_de_compras:
    print(coisa)

#Slice
print(minha_lista_de_compras[0])
print(minha_lista_de_compras[1])
print(minha_lista_de_compras[1:])
print(minha_lista_de_compras[3:])
print(minha_lista_de_compras[:3])

#Exemplo
# n = [0, 2, 3, 4,  5, 6, 7, 8, 9]
# n[0] = 0
# n[6:] = 6, 7, 8, 9
# n[:-6] = 0, 1, 2, 3
# n[::2] = 0, 2, 4, 6 Imprimindo apenas os pares
