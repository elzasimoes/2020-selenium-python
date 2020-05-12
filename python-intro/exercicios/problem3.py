#Quantos metros
#1L para cada 3 metros
#Lata tem 18L
#Preço 80,00

#Informe ao usuário a quantidade de latas de tinta a serem
#compradas e o preço total

metros = float(input('Digite os metros quadrados: '))
litros = metros / 3

preco_litro = 80.00
capacidade_litro = 18

latas = litros / capacidade_litro
total = latas * preco_litro

print(f'Você usara {latas} latas de tinta')
print(f'O preço total é de R${total} reais')
