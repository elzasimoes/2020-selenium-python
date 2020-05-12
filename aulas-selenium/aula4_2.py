from selenium.webdriver import Chrome
from time import sleep

def find_by_text(browser, tag, text):
    '''
    Encontrar o elemento com o texto 'text'

    Argumentos:
        - browser = Instancia do Browser[firefox, chrome, ..]
        - texto = conteudo que deve estar na tag
        - tag = tag onde o texto será procurado
    '''
    elementos = browser.find_elements_by_tag_name(tag) #Lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

sleep(1)

def find_by_href(browser, link):

    '''
    Encontrar o elemento "a" com o link 'text'

    Argumentos:
        - browser = Instancia do Browser[firefox, chrome, ..]
        - link - link que será procurado em todos os 'a'
    '''
    elementos = browser.find_elements_by_tag_name('a')

    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento


browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

# elemento_ddg = find_by_text(browser,'li', 'a')

elemento_ddg = find_by_href(browser,'ddg')
