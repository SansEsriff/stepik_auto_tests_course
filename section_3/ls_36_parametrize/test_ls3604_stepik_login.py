import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

"""Фикстура открытия браузера browser подтягивается автоматически из conftest.py"""

links = [
        "https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
        ]


class TestStepik:

    solution = []

    @staticmethod
    def stepik_login(browser):
        # find login button, enter credentials
        login_button = WebDriverWait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_button.click()
        browser.find_element(By.ID, "id_login_email").send_keys("****")
        browser.find_element(By.ID, "id_login_password").send_keys("****")
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        # wait for profile button and answer text area to be loaded
        WebDriverWait(browser, 30).until(
            expected_conditions.
            visibility_of_element_located((By.CSS_SELECTOR, "button.navbar__profile-toggler"))
        )

    @staticmethod
    def stepik_submit_answer(browser, ans):
        # find text area and check if it's possible to pass the answer
        answer_text_area = WebDriverWait(browser, 30).until(
            expected_conditions.
            visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        browser.execute_script("return arguments[0].scrollIntoView(true);", answer_text_area)
        answer_text_area_disabled = answer_text_area.get_attribute("disabled")

        if not answer_text_area_disabled:
            answer_text_area.send_keys(Keys.CONTROL + "A")
            answer_text_area.send_keys(ans)
        else:
            solve_again_button = WebDriverWait(browser, 30).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
            )
            solve_again_button.click()
            answer_text_area = WebDriverWait(browser, 30).until(
                expected_conditions.
                visibility_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
            )
            answer_text_area.send_keys(ans)

        # press the "submit" button as soon as it becomes clickable
        submit_button = WebDriverWait(browser, 30).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        submit_button.click()

    @pytest.mark.parametrize("link", links)
    def test_stepik_find_solution(self, browser, link):
        browser.implicitly_wait(30)
        browser.get(link)
        self.stepik_login(browser)
        answer = math.log(int(time.time()))
        self.stepik_submit_answer(browser, answer)

        # find optional feedback field and check if answer is correct, otherwise
        # add error text to sollution list
        optional_feedback = WebDriverWait(browser, 30).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
            )
        text = optional_feedback.text
        if text == "Correct!":
            assert True
        else:
            self.solution.append(text)
            print(f"Secret message {text} found!!!")
            assert False

    def test_send_solution(self, browser):
        browser.implicitly_wait(30)
        browser.get("https://stepik.org/")
        self.stepik_login(browser)
        browser.get("https://stepik.org/lesson/237240/step/5")
        stepik_solution = "".join(self.solution)
        self.stepik_submit_answer(browser, stepik_solution)
        optional_feedback = WebDriverWait(browser, 30).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))
        )
        text = optional_feedback.text
        assert text == "Correct!", "Неверный ответ!"
