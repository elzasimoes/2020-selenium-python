from unittest import TestCase, main
from parimpar import numero_par, numero_impar
"""
TDD = Test Driven Development
"""

class Testes(TestCase):
    """
    Verificar se o valor é par ou impar
    """
    def teste_par(self):
        self.assertEqual(numero_par(2), True)
    def teste_impar(self):
        self.assertEqual(numero_impar(3), True)

    """
    Verificar se é string
    """
    def teste_string(self):
        self.assertEqual(numero_par('string'), False)

if __name__ == '__main__':
    main()
