# language: pt
# pip install behave

Funcionalidade: Calc
    Cenario: adicao basica
      Quando somar "2" com "2"
      Entao o resultado deve ser "4"

      Cenario: adicao ponto flutuante
        Quando somar "2.0" com "2.0"
        Entao o resultado deve ser "4.0"
