##Combinatória de dois elementos e nos retorne as combinações em uma nova lista.
#Exemplo de entrada: [1, 2, 3, 4]
#Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

from itertools import product

caracteres = [1, 2, 3, 4]
permsList = list(product(caracteres, repeat=2))
print(permsList)
