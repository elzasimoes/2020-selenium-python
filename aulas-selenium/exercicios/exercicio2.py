from selenium.webdriver import Chrome
from time import sleep

url = 'http://selenium.dunossauro.live/exercicio_02.html'
navegador = Chrome()
navegador.get(url)
sleep(1)

a = navegador.find_element_by_tag_name('a')
msg = ''

while 'Você ganhou' not in msg:
    a.click()
    msg = navegador.find_elements_by_tag_name('p')[-1].text

sleep(3)
navegador.quit()
