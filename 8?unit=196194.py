from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

driver.get("http://suninjuly.github.io/find_xpath_form")

input1 = driver.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = driver.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = driver.find_element_by_name("firstname")
input3.send_keys("Smolensk")
input4 = driver.find_element_by_id("country")
input4.send_keys("Russia")
button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
button.click()