from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name='firstname']").send_keys("Axultan")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("Raikhanov")
    browser.find_element_by_css_selector("[name='email']").send_keys("123@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file_3_4_3.txt")
    browser.find_element_by_css_selector("input[type='file']").send_keys(file_path)

    browser.find_element_by_css_selector(".btn.btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()
