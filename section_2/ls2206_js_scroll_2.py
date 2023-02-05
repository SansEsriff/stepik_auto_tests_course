from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    # Открыть страницу
    browser.get(link)

    # Считать значение для переменной x
    x = browser.find_element(By.ID, "input_value").text

    # Посчитать математическую функцию от x
    res = calc(x)

    # Проскроллить страницу вниз
    browser.execute_script("window.scrollBy(0, 200);")

    # Ввести ответ в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(res)

    # Выбрать checkbox "I'm the robot"
    browser.find_element(By.ID, "robotCheckbox").click()

    # Переключить radiobutton "Robots rule!"
    browser.find_element(By.ID, "robotsRule").click()

    # Нажать на кнопку "Submit"
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()

"""
Как вариант еще можно скрывать ненужный элемент

browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body

from selenium.webdriver.common.keys import Keys
browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
"""





