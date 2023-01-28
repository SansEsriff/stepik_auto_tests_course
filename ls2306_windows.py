from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    # Открыть страницу
    browser.get(link)

    # Нажать на кнопку
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn").click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Нажать кнопку "Submit"
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()


""" Авторизация на Stepik
alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]

browser.get('https://stepik.org/catalog?auth=login&language=ru')
time.sleep(5)

browser.find_element_by_id('id_login_email').send_keys('***')# здесь вводится e-mail
browser.find_element_by_id('id_login_password').send_keys('***')# здесь вводится пароль

browser.find_element_by_class_name('sign-form__btn').click()
time.sleep(3)
browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
time.sleep(3)

answer_input = browser.find_element_by_css_selector('textarea')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(answer)

button = browser.find_element_by_class_name('submit-submission')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(1)
button.click()"""