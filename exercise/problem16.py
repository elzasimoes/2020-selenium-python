#Faça um programa, com uma função, que calcula a média de uma lista.
#Funções embutidas que podem te ajudar:
#● len(lista) -> calcula o tamanho da lista
#● sum(lista) -> faz o somatório dos valores

notas = [0, 0, 9.0, 8.0, 5.0, 10.0, 7.0, 7.5, 4.0, 10.0, 7.0, 7.0, 8.0, 8.0, 7.5]

soma_das_notas = sum(notas)
print(soma_das_notas)

qtd_de_notas = len(notas)
print(qtd_de_notas)

media_das_notas = soma_das_notas / qtd_de_notas
print(media_das_notas)
