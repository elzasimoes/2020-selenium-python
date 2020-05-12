from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_05_a.html'

chrome = Chrome()

chrome.get(url)

# div_1 = chrome.find_element_by_tag_name('div')

div_py = chrome.find_element_by_id('python')
div_hk = chrome.find_element_by_id('haskell')

sleep(1)

pprint(f"O conteúdo do id='haskell' é: {div_hk.text}")

chrome.quit()
