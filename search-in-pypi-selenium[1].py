from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search = input("Enter what you want to search: ")
driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/")
input_element = driver.find_element(By.NAME, "q")
# print(input_element)
input_element.clear()
input_element.send_keys(search + Keys.ENTER)

time.sleep(555555)
driver.quit()
