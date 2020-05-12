from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element_by_tag_name('ul') #1
lis = lista_n_ordenada.find_elements_by_tag_name('li') #2

lis[0].find_element_by_tag_name('a').text #3

'''
1. Buscamos "ul".
2. Buscamos todos "li".
3. No primeiro "li", buscamos "a" e pegamos o seu texto.

'''
