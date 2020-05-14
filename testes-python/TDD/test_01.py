from unittest import TestCase, main
'''TDD'''

def soma(y, x):
    return y + x

def sub(y, x):
    return y - x

def mult(y, x):
    return y * x

def div(y, x):
    return y / x

class Testes(TestCase):
    '''Verificando se o valor da soma é menor que 11'''
    def teste_soma1(self):
        self.assertLess(soma(5, 5), 11)
    '''Verificando se o valor da soma é 10'''
    def teste_soma2(self):
        self.assertEqual(soma(5, 5), 10)
    '''Verificando se o valor é IGUAL ou MENOR'''
    def teste_soma3(self):
        self.assertLessEqual(soma(5, 5), 10)

    def teste_sub(self):
        self.assertEqual(sub(5, 5), 0)
    def teste_mult(self):
        self.assertEqual(mult(5, 5), 25)
    def teste_div(self):
        self.assertEqual(div(10, 2), 5)

    '''Testando soma errada para verificar o output
    AssertionError: 20 != 15
    def teste_soma_errada(self):
        self.assertEqual(soma(10, 10), 15)'''

if __name__ == '__main__':
    main()
