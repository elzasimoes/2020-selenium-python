from unittest import TestCase, main
'''TDD'''

def numero_par(valor):
    return True if valor % 2 == 0 else False

def numero_impar(valor):
    return True if valor % 2 != 0 else False

class Testes(TestCase):
    '''Se o valor é par ou impar'''
    def teste_par(self):
        self.assertEqual(numero_par(2), True)
    def teste_impar(self):
        self.assertEqual(numero_impar(3), True)

if __name__ == '__main__':
    main()
