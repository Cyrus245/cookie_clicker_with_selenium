from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element(By.NAME, "fName")
fName.send_keys("Cyrus")
lName = driver.find_element(By.NAME, "lName")
lName.send_keys("Sakib")
email = driver.find_element(By.NAME, "email")
email.send_keys("cs@gmail.com")
button = driver.find_element(By.XPATH, '/html/body/form/button')
button.click()
time.sleep(180)
