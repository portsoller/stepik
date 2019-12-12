from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

driver.get("http://suninjuly.github.io/huge_form.html")
assert "Very long form" in driver.title


try:
    elements = driver.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Мой")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла