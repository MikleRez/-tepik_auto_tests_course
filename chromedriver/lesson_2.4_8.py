import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Открыть страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

#Дождаться, когда цена дома уменьшится до $100
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )

# Нажать на кнопку "Book"
button_book = browser.find_element(By.ID, "book")
button_book.click()

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
button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)
browser.close()

