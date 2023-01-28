from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    # Открыть страницу
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("Vasya")
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("viper@gmail.com")

    # Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(dir_path, "file_ls2208.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()


