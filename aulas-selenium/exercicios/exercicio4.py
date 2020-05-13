from selenium.webdriver import Chrome
from urllib.parse import urlparse
from time import  sleep
from json import loads



browser = Chrome()
browser.get('https://selenium.dunossauro.live/exercicio_04.html')

sleep(2)

def preencher_formulario(browser, nome, email, senha, telefone):
    browser.find_element_by_name('nome').send_keys(nome)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('senha').send_keys(senha)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('btn').click()



dados = {
        'nome':'Pode me chamar de Elza',
        'email':'elzaesimoes@gmail.com',
        'senha':'123456',
        'telefone':'994698246'
}

preencher_formulario(browser, **dados)


sleep(2)


url_parseada = urlparse(browser.current_url)
sleep(2)



textarea = browser.find_element_by_tag_name('textarea').text
resultado = textarea.replace('\'', '\"')
resultado = loads(resultado)

assert textarea == resultado
print('Os dados são iguais')
sleep(2)
browser.quit()
