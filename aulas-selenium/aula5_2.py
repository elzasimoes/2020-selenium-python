from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_05_b.html'
chrome = Chrome()
chrome.get(url)

topico = chrome.find_element_by_class_name('topico')
linguagens = chrome.find_elements_by_class_name('linguagens')

for linguagem in linguagens:
    pprint((linguagem.find_element_by_tag_name('h2').text,
             linguagem.find_element_by_tag_name('p').text))
