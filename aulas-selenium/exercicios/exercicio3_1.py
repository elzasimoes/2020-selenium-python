from selenium.webdriver import Chrome
from time import sleep
from urllib.parse import urlparse

url = 'https://selenium.dunossauro.live/exercicio_03.html'

#Função para encontrar attr = errado
def find_a_by_attr(browser, attr, valor):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.get_attribute(attr) == valor:
            return elemento

#Função que encontra o titulo da pagina.
def find_a_by_content(browser, content):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if elemento.text == content:
            return elemento

browser = Chrome()
browser.get(url)

# Pagina 1
sleep(3)
main = browser.find_element_by_tag_name('main')
main.find_element_by_tag_name('a').click()

# Pagina 2
sleep(3)
main = browser.find_element_by_tag_name('main')
find_a_by_attr(main, 'attr', 'errado').click()

# Pagina 3
sleep(10)
browser.refresh()
sleep(2)
main = browser.find_element_by_tag_name('main')
titulo = browser.title
find_a_by_content(main, browser.title).click()

# Pagina 4
sleep(2)
browser.find_element_by_link_text("page_3.html").click()
#parsed_url = urlparse(browser.current_url)
#find_a_by_content(main, parsed_url.path[1:]).click()

# Pagina Chefão
sleep(3)
browser.refresh()
