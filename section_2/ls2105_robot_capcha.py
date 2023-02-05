from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


# Функция по расчету значения капчи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Открыть страницу
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x и вычислить результат
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
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
