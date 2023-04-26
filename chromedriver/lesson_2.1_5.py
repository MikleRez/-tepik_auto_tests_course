from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(executable_path="C:\\Users\\MikleRez\\PycharmProjects\\chromedriver\\chromedriver.exe")
import time
import math

# Описать функцию
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открыть страницу
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)
    # Считать значение x
    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    # Расcчитать значение функции
    y = calc(x)
    print(y)
    # Ввести ответ в текстовое поле
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    # Отметить checkbox "Подтверждаю, что являюсь роботом"
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()
    # Выбрать radiobutton "Роботы рулят!"
    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()
    # Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(10)

finally:
    browser.close()
    browser.quit()