import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def registration(link):
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("Vasya")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("vasya@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

    finally:
        time.sleep(5)
        browser.quit()

    return welcome_text


class TestRegistration(unittest.TestCase):

    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        result = registration(link)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(result, "Congratulations! You have successfully registered!",
                         f"Registration failed! Returned {result}")

    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        result = registration(link)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(result, "Congratulations! You have successfully registered!",
                         f"Registration failed! Returned {result}")


if __name__ == "__main__":
    unittest.main()
