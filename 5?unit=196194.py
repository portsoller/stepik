from selenium import webdriver
import math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

driver.get("http://suninjuly.github.io/find_link_text")
assert "Simple registration form" in driver.title

# find volume

test = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(test)

link = driver.find_element_by_link_text(test)
link.click()

# fill form

input1 = driver.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = driver.find_element_by_name("last_name")
input2.send_keys("Petrov")
input3 = driver.find_element_by_name("firstname")
input3.send_keys("Smolensk")
input4 = driver.find_element_by_id("country")
input4.send_keys("Russia")
button = driver.find_element_by_css_selector("button.btn")
button.click()