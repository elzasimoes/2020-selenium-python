from behave import step
from calc import soma

@step('somar "{valor_0}" com "{valor_1}"')
def test_soma(context, valor_0, valor_1):
    context.result = float(soma(float(valor_0), float(valor_1)))

@step('o resultado deve ser "{resultado}"')
def test_soma_result(context, resultado):
    assert context.result == float(resultado)
