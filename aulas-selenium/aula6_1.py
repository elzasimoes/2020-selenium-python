from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()

url = 'https://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)
"""
# Usando o atributo type
nome = browser.find_element_by_css_selector('[type="text"]')
senha = browser.find_element_by_css_selector('[type="password"]')
btn = browser.find_element_by_css_selector('[type="submit"]')

# Usando o atributo name
nome = browser.find_element_by_css_selector('[name="nome"]')
senha = browser.find_element_by_css_selector('[name="senha"]')
btn = browser.find_element_by_css_selector('[name="l0c0"]')

#Usando o atributo * [attr*=valor]
nome = browser.find_element_by_css_selector('[name*="ome"]')
senha = browser.find_element_by_css_selector('[name*="nha"]')
btn = browser.find_element_by_css_selector('[name*="l0"]')

#Usando o atributo | [attr|=valor]
nome = browser.find_element_by_css_selector('[name^="n"]')
senha = browser.find_element_by_css_selector('[name^="s"]')
btn = browser.find_element_by_css_selector('[name^="l"]')
"""
#Usando o atributo ^ [attr^=valor]

nome = browser.find_element_by_css_selector('[name^="n"]')
senha = browser.find_element_by_css_selector('[name^="s"]')
btn = browser.find_element_by_css_selector('[name^="l"]')

nome.send_keys('Elza Simões de Oliveira')
sleep(2)
senha.send_keys('1234dsa')
sleep(2)
btn.click()
