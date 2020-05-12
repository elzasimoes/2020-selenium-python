from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    sleep(1)
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(1)
    browser.back()

for nome in nomes_das_caixas:
    sleep(1)
    browser.forward()
