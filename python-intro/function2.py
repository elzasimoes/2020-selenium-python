#sum -> soma
#len -> tamanho

def soma(numero_1, numero_2):
    return numero_1 + numero_2

def media(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)

def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relatório parcial

    {nome}, portador do cpf {cpf}, usuário do telefone {telefone} está oficialmente de férias

    Ass: Direção
    """

print(imprime_relatorio( nome='Elza Simões', cpf=232312312, telefone=99423424))
