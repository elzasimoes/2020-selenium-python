from selenium.webdriver import Chrome

# mode headless

url = 'http://selenium.dunossauro.live/exercicio_01.html'
navegador = Chrome()
navegador.get(url)

h1 = navegador.find_element_by_tag_name('h1').text
ps = navegador.find_elements_by_tag_name('p')

attrs = []
texts = []

for p in ps:
    attrs.append(p.get_attribute('atributo'))

for p in ps:
    texts.append(p.text)

print({h1: dict(zip(attrs, texts))})
