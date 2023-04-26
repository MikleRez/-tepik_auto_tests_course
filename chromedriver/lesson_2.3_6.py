import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    result = []
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    knopka = browser.find_element(By.CSS_SELECTOR, "button.btn")
    knopka.click()
    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]  # Нашли 2ую по счету вкладку в браузере
    first_window = browser.window_handles[0]  # Запомнили предыдущую вкладку на всякий случай
    browser.switch_to.window(new_window)  # Переключились на новую вкладку


    # Описать функцию
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Считать значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Расcчитать значение функции
    y = calc(x)

    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    # Нажать на кнопку Отправить
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)
    browser.close()
