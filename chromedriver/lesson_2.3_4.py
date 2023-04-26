from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Открыть страницу
link = "http://suninjuly.github.io/alert_accept.html"
brow = webdriver.Chrome()
brow.get(link)

# Нажать кнопку
knopka = brow.find_element(By.CSS_SELECTOR, "button.btn")
knopka.click()

# Принять confirm
confirm = brow.switch_to.alert
confirm.accept()

# Описать функцию
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Считать значение x
x_element = brow.find_element(By.ID, "input_value")
x = x_element.text

# Расcчитать значение функции
y = calc(x)

# Ввести ответ в текстовое поле
answer = brow.find_element(By.ID, "answer")
answer.send_keys(y)

# Нажать на кнопку Отправить
button = brow.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
brow.close()