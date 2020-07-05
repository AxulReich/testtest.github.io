from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
link_2 = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link_2)

    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    ans = int(a) + int(b)

    # browser.find_element_by_id('dropdown').click()
    # browser.find_element_by_css_selector(f"[value='{ans}']").click()

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(ans))
    browser.find_element_by_css_selector(".btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()