import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

"""
Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks). 
Для маркировки теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — 
произвольная строка.

Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
pytest -s -v -m smoke test_fixture8.py
pytest -s -v -m "not smoke" test_fixture8.py
pytest -s -v -m "smoke or regression" test_fixture8.py
pytest -s -v -m "smoke and win10" test_fixture81.py

Как регистрировать метки?
Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:

[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win10

Текст после знака ":" является поясняющим — его можно не писать.

Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip

Чтобы помечать тест как ожидаемо падающий добавим маркировку @pytest.mark.xfail
pytest -rx -v test_fixture10a.py
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
