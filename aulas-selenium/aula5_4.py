from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/aula_05.html'

chrome = Chrome()

chrome.get(url)

chrome.set_window_size(1382, 744)

def preencher_formulario(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()


sleep(2)

dados = {
        'nome':'Pode me chamar de Elza',
        'email':'elzaesimoes@gmail.com',
        'senha':'123456',
        'telefone':'994698246'
}

preencher_formulario(chrome, **dados)

url_parseada = urlparse(chrome.current_url)

sleep(2)

texto_resultado = chrome.find_element_by_id('result').text
resultado_arrumado = texto_resultado.replace('\'', "\"")
dic_result = loads(resultado_arrumado)

sleep(5)
chrome.refresh()
chrome.quit()

#? Query String.
