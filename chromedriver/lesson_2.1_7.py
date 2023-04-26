from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
#открыть ссылку
    browser = webdriver.Chrome(executable_path="C:\\Users\\MikleRez\\PycharmProjects\\chromedriver\\chromedriver.exe")
    browser.get("http://suninjuly.github.io/get_attribute.html")
#Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    img = browser.find_element(By.ID, "treasure")

#Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x_element = img.get_attribute("valuex")
    print(x_element)

#Посчитать математическую функцию от x (сама функция остаётся неизменной).
    y = calc(x_element)
    print(y)

#Ввести ответ в текстовое поле.
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

#Отметить checkbox "I'm the robot".
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

#Выбрать radiobutton "Robots rule!".
    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

#Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)
finally:
    browser.close()
    browser.quit()

