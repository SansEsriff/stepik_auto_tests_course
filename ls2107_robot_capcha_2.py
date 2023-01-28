from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Функция по расчету значения капчи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами
    image = browser.find_element(By.ID, "treasure")
    x = image.get_attribute("valuex")
    result = calc(x)

    # Ввести ответ в текстовое поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)

    # Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!"
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
