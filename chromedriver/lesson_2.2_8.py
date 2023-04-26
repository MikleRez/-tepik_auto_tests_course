from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Заполнение полей
f_name = browser.find_element(By.NAME, "firstname").send_keys("Вова")
l_name = browser.find_element(By.NAME, "lastname").send_keys("Вовинский")
email = browser.find_element(By.NAME, "email").send_keys("test@test.ru")

Choose_file = browser.find_element(By.ID, "file")  #находим кнопку загрузить файл
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
print(file_path)
Choose_file.send_keys(file_path)

# Нажать на кнопку Отправить
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
browser.close()
browser.quit()
