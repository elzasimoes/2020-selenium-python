from selenium.webdriver import Chrome
from time import sleep

url = 'http://127.0.0.1:8080/'

browser = Chrome()
browser.get(url)

print(browser.page_source)
