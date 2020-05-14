def numero_par(valor: int) -> bool:
    try:
        return True if valor % 2 == 0 else False
    except TypeError:
        return False

def numero_impar(valor):
    return True if valor % 2 != 0 else False
