from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_03.html'

chrome = Chrome()

chrome.get(url)

chrome.set_window_size(1382, 744)

def jogar_diabao(browser):
    print('Pagina de start no jogo')
    #Valor não muda
    browser.find_element_by_link_text("Começar por aqui").click()
    print('Primeira pagina do jogo')
    sleep(5)
    #Valores mudam
    browser.find_element_by_css_selector("a[attr='errado']").click()
    print('Segunda página do jogo, quando clica a pagina buga então fiz uma gambiarra pra funcionar heheh, espere')
    sleep(15)
    browser.refresh()
    sleep(5)
    browser.find_element_by_xpath("//a[contains(@href, \'page_3.html\')]").click()
    print('Terceira página do jogo')
    #Valor não muda
    sleep(5)
    browser.find_element_by_link_text("page_3.html").click()
    print('Quarta pagina do jogo, a salvação')
    sleep(2)
    browser.refresh()
    print('uhull, você venceu')

jogar_diabao(chrome)
