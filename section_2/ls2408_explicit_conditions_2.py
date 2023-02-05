import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Функция по расчету значения капчи
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# Открыть страницу
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100
    # (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # Нажать на кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    # Считать значение для переменной x и вычислить результат
    x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text
    result = calc(x)

    # Ввести ответ в текстовое поле
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(result)

    # Нажать на кнопку Submit
    button = browser.find_element(By.ID, "solve")
    button.click()


finally:
    time.sleep(10)
    browser.quit()
