import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_registration(self):
        link = "http://suninjuly.github.io/registration1.html"
        # link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(link)

        input_name = browser.find_element_by_xpath("//input[@required][@class='form-control first']")
        input_name.send_keys('vanya')
        input_lastname = browser.find_element_by_xpath("//input[@required][@class='form-control second']")
        input_lastname.send_keys('ivanov')
        input_email = browser.find_element_by_xpath("//input[@required][@class='form-control third']")
        input_email.send_keys('fes@fse.com')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_text, "Mismatch expected congratulation text with given text")
        browser.quit()

    def test_registration_2_test(self):
        # link = "http://suninjuly.github.io/registration1.html"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(link)

        input_name = browser.find_element_by_xpath("//input[@required][@class='form-control first']")
        input_name.send_keys('vanya')
        input_lastname = browser.find_element_by_xpath("//input[@required][@class='form-control second']")
        input_lastname.send_keys('ivanov')
        input_email = browser.find_element_by_xpath("//input[@required][@class='form-control third']")
        input_email.send_keys('fes@fse.com')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_text, "Mismatch expected congratulation text with given text")
        browser.quit()


if __name__ == '__main__':
    unittest.main()
