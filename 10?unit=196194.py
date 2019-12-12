from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

try:
    driver.get("http://suninjuly.github.io/registration1.html")
    # driver.get("http://suninjuly.github.io/registration2.html")

    # Ваш код, который заполняет обязательные поля
    content = driver.find_element_by_class_name('first')
    content.send_keys("Ivan")
    input2 = driver.find_element_by_class_name('second')
    input2.send_keys("Petrov")
    input3 = driver.find_element_by_class_name('third')
    input3.send_keys("test123@gmail.com")
    # input4 = driver.find_element_by_id("country")
    # input4.send_keys("Russia")
    # button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
    # button.click()

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()