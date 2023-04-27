from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

# Считать значение x
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text

# Расcчитать значение функции
y = calc(x)

# Вывод результата в консоль
print(y)

# Ввести ответ в текстовое поле
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)

# Выбрать checkbox "I'm the robot"
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

# Скролим страницу вниз
robotsRule = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

# Нажать на кнопку Отправить
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.close()
browser.quit()
