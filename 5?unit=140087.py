from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# путь и опции драйвера браузера.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

driver.get("http://suninjuly.github.io/math.html")



x_element = driver.find_element_by_id('input_value')
x = x_element.text
y = calc(x)
print(y)

option1 = driver.find_element_by_id("robotCheckbox")
option1.click()

option2 = driver.find_element_by_id("answer")
option2.send_keys(y)


option3 = driver.find_element_by_css_selector("[for='robotsRule']")
option3.click()

submit = driver.find_element_by_class_name("btn")
submit.click()


