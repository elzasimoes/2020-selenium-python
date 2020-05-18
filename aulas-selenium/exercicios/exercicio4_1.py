from selenium.webdriver import Chrome
from urllib.parse import urlparse, parse_qsl
from time import  sleep
from json import loads


url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Chrome()
browser.get(url)

sleep(2)

form = {
        'nome': browser.find_element_by_name('nome'),
        'email': browser.find_element_by_name('email'),
        'senha': browser.find_element_by_name('senha'),
        'telefone': browser.find_element_by_name('telefone'),
        'btn': browser.find_element_by_name('btn')
}

form['nome'].send_keys('Elza')
form['email'].send_keys('elza@uol.com.br')
form['senha'].send_keys('123smaks')
form['telefone'].send_keys('994698246')
form['btn'].click()


# -------------------- parte 2
sleep(2)
dict_textarea = eval(browser.find_element_by_tag_name('textarea').text)
dict_url = dict(parse_qsl(urlparse(browser.current_url).query))

dict_url.pop('btn')

assert dict_textarea == dict_url
