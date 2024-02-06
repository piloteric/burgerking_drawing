from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# BK URL
url = "https://www.burgerking.com.tw/blog/75135"
 
# Options
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# OPEN THE DOOR
driver.get(url)
# Wait for Script loading
time.sleep(3)
click_wheel = driver.find_element(By.XPATH,"//div[2]/div[3]/button").click()