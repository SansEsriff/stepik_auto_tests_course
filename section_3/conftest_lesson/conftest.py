import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Фикстуру можно вынести в отдельный файл conftest.py"""

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
