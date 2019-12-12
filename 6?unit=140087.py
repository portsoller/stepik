from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# путь и опции драйвера браузера.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless")
browser = webdriver.Chrome("/home/abramenko/Python3/chromedriver",
chrome_options=chrome_options)

browser.get("http://suninjuly.github.io/math.html")

people_radio = browser.find_element_by_id("peopleRule")