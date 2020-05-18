from selenium.webdriver import Chrome
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_05.html'

browser = Chrome()

browser.get(url)

def forml0c0(browser):
    browser.find_element_by_css_selector(".form-l0c0 > .form-group:nth-child(2) > input").click()
    browser.find_element_by_css_selector(".form-l0c0 > .form-group:nth-child(2) > input").send_keys("preenchendo primeiro")
    browser.find_element_by_css_selector(".form-l0c0 > .form-group:nth-child(4) > input").click()
    browser.find_element_by_css_selector(".form-l0c0 > .form-group:nth-child(4) > input").send_keys("123")
    browser.find_element_by_css_selector(".form-l0c0 > .form-btn > input").click()

def forml0c1(browser):
    browser.find_element_by_css_selector(".form-l0c1 > .form-group:nth-child(2) > input").click()
    browser.find_element_by_css_selector(".form-l0c1 > .form-group:nth-child(2) > input").send_keys("preenchendo segundo")
    browser.find_element_by_css_selector(".form-l0c1 > .form-group:nth-child(4) > input").click()
    browser.find_element_by_css_selector(".form-l0c1 > .form-group:nth-child(4) > input").send_keys("345")
    browser.find_element_by_css_selector(".form-l0c1 > .form-btn > input").click()

def forml1c0(browser):
    browser.find_element_by_css_selector(".form-l1c0 > .form-group:nth-child(2) > input").click()
    browser.find_element_by_css_selector(".form-l1c0 > .form-group:nth-child(2) > input").send_keys("preenchendo quarto")
    browser.find_element_by_css_selector(".form-l1c0 > .form-group:nth-child(4) > input").click()
    browser.find_element_by_css_selector(".form-l1c0 > .form-group:nth-child(4) > input").send_keys("678")
    browser.find_element_by_css_selector(".form-l1c0 > .form-btn > input").click()

def forml1c1(browser):
    browser.find_element_by_css_selector(".form-l1c1 > .form-group:nth-child(2) > input").click()
    browser.find_element_by_css_selector(".form-l1c1 > .form-group:nth-child(2) > input").send_keys("preenchendo ultimo")
    browser.find_element_by_css_selector(".form-l1c1 > .form-group:nth-child(4) > input").click()
    browser.find_element_by_css_selector(".form-l1c1 > .form-group:nth-child(4) > input").send_keys("91011")
    browser.find_element_by_css_selector(".form-l1c1 > .form-btn > input").click()


if __name__ == '__main__':
    while True:
        forml0c0(browser)
        sleep(1)
        forml0c1(browser)
        sleep(1)
        forml1c0(browser)
        sleep(1)
        forml1c1(browser)
        sleep(2)
        browser.refresh()
