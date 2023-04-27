from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

class TestWelcome(unittest.TestCase):

	def test_welcome_text1(self):
		browser = webdriver.Chrome()
		browser.get(link1)
# Ваш код, который заполняет обязательные поля
		name = browser.find_element(By.CSS_SELECTOR, "first_block .first")
		name.send_keys("Мое имя")
		first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
		first_name.send_keys("Моя фамилия")
		email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
		email.send_keys("Моя почта")
# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
		time.sleep(1)
# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Welcom text не совпадает с ожидаемым '{}'".format(welcome_text))

	def test_welcome_text2(self):
		browser = webdriver.Chrome()
		browser.get(link2)
# Ваш код, который заполняет обязательные поля
		name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
		name.send_keys("Мое имя")
		first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
		first_name.send_keys("Моя фамилия")
		email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
		email.send_keys("Моя почта")
# Отправляем заполненную форму
		button = browser.find_element(By.CSS_SELECTOR, "button.btn")
		button.click()
# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
		time.sleep(1)
# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
		self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!", "Welcom text не совпадает с ожидаемым '{}'".format(welcome_text))

if __name__ == "__main__":
    unittest.main()