from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('button.trollface.btn.btn-primary').click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))

    browser.find_element_by_id('answer').send_keys(str(y))
    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
