from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("div.container .btn.btn-primary").click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    browser.find_element_by_id('answer').send_keys(str(y))

    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
