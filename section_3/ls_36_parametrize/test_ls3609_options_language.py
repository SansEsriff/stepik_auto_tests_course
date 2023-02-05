"""
Браузер передает данные о языке пользователя через запросы к серверу, указывая
в Headers (заголовке запроса) параметр accept-language. Если сервер получит запрос
с заголовком {accept-language: ru, en}, то он отобразит пользователю русскоязычный
интерфейс сайта. Если русский язык не поддерживается, то будет показан следующий язык
из списка, в данном случае пользователь увидит англоязычный интерфейс.

Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и
метод add_experimental_option, как указано в примере ниже:
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as Firefox_Options


# for Chrome
options_chrome = Chrome_Options()
options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)

# for Firefox
options_ff = Firefox_Options()
options_ff.set_preference('intl.accept_languages', user_language)
browser = webdriver.Firefox(options=options_ff)
