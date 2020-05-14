from behave import step_matcher
from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()
url = 'http://127.0.0.1:8080/'

@step("acessar a pagina '{page}'")
def acess_page(context, index):
    browser.get(url)

sleep(3)

@step('deve aparecer "{string}"')
def test_html(context, string):
    assert string in browser.page_source, "O texto não foi encontrado na página"
