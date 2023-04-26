from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

    # Открыть страницу
browser = webdriver.Chrome()
browser.get(link)

    # Посчитать сумму заданных чисел
num1 = browser.find_element(By.ID, "num1").text
num2 = browser.find_element(By.ID, "num2").text
sum = int(num1) + int(num2)
print(str(sum))

    # Выбрать в выпадающем списке значение равное расчитанной сумме
select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))

    # Нажать кнопку "Submit"
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(5)
browser.close()
browser.quit()
