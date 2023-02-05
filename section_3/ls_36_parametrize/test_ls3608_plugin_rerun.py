"""
Мы будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг,
а не упал случайно.
Это сделать очень просто. Для этого мы будем использовать плагин pytest-rerunfailures.
pip install pytest-rerunfailures
"""
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")
