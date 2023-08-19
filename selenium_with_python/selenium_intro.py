from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get(
    "https://www.amazon.com/beyerdynamic-770-PRO-Studio-Headphone/dp/B0016MNAAI/ref=sr_1_6?keywords=Beyerdynamic%2Bdt"
    "%2B770%2Bpro&qid=1691130533&sr=8-6&th=1")

# finding an  element using class name
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# finding an element by id
title = driver.find_element(By.ID, 'productTitle')
# finding an element by XPATH
note = driver.find_element(By.XPATH, '//*[@id="universal-product-alert"]/div/span[2]')
# finding an element  by input name
input_box = driver.find_element(By.NAME, "field-keywords")
# clearing an element
input_box.clear()
# typing into an input
input_box.send_keys("Fuck you")
# typing into an input and pressing enter key
input_box.send_keys("Fuck you", Keys.ENTER)

print(title.text)
print(price.text)
# driver.quit()
