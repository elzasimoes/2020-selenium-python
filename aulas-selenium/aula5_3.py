from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/aula_05_c.html'

chrome = Chrome()

chrome.get(url)

chrome.set_window_size(1382, 744)

def preencher_filme(browser, filme, email, telefone):
    """
        Função para preencher o formulário do melhor filme de 2020.
    """
    browser.find_element_by_name('filme').send_keys(filme)
    browser.find_element_by_name('email').send_keys(email)
    browser.find_element_by_name('telefone').send_keys(telefone)
    browser.find_element_by_name('enviar').click()


preencher_filme(chrome,
                'Parasita',
                'elzaesimoes@gmail.com',
                '92994698246')

sleep(2)
chrome.refresh()

preencher_filme(chrome,
                'Minha mãe é uma peça',
                'fulano@gmail.com',
                '92994657637')

sleep(2)
chrome.quit()
