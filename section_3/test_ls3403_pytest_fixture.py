import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

"""
Метод browser является фикстурой с помощью декоратора @pytest.fixture. 
После этого мы можем вызывать фикстуру в тестах, передав ее как параметр. 
По умолчанию фикстура будет создаваться для каждого тестового метода, то есть для каждого теста 
запустится свой экземпляр браузера.

Один из вариантов финализатора — использование ключевого слова Python: yield. 
После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, 
следующей за строкой со словом yield

Для фикстур можно задавать область покрытия фикстур. Допустимые значения: 
“function”, “class”, “module”, “session”. Соответственно, фикстура будет вызываться 
только один раз для тестового метода, только один раз для класса, только один раз для модуля 
или только один раз для всех тестов, запущенных в данной сессии. 

При описании фикстуры можно указать дополнительный параметр autouse=True, который укажет, 
что фикстуру нужно запустить для каждого теста даже без явного вызова
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
