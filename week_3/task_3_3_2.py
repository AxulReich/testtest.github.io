from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_xpath("//img").get_attribute('valuex')
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_css_selector(".btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()