from selenium.webdriver import Chrome
from time import sleep

browser = Chrome()

url = 'https://selenium.dunossauro.live/aula_06_a.html'

browser.get(url)

#Br irmão de div class form-group
browser.find_elements_by_css_selector('div.form-group + br')[1].get_attribute('id')
# Da tag div com a classe form-group pegue o filho com id dentro-nome
browser.find_element_by_css_selector('div.form-group > #dentro-nome')
# Do form, pegue todas as labels existentes, ignorando a hierarquia. (Descendente)
browser.find_elements_by_css_selector('form label')
