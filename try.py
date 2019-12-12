import unittest
from selenium import webdriver
import time

# путь и опции драйвера браузера.
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--window-size=1000,800")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"


class TestSelectors(unittest.TestCase):
    def test_page1(self):
        driver.get(url1)
        # Ваш код, который заполняет обязательные поля
        input1 = driver.find_element_by_xpath("//div[1]/input")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//div[2]/input")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_xpath("//div[3]/input")
        input3.send_keys("test123@gmail.com")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)
        self.assertTrue("registration_result" in driver.current_url)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        #driver.quit()

    def test_page2(self):
        driver.get(url2)
        # Ваш код, который заполняет обязательные поля
        input1 = driver.find_element_by_xpath("//div[1]/input")
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//div[2]/input")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_xpath("//div[3]/input")
        input3.send_keys("test123@gmail.com")

        # Отправляем заполненную форму
        button = driver.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text
        # self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)
        self.assertTrue("registration_result" in driver.current_url)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        driver.quit()


if __name__ == "__main__":
    unittest.main()