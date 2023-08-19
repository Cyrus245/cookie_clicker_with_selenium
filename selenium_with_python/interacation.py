from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

no_of_article = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(no_of_article)
homepage = driver.find_element(By.LINK_TEXT, "Wikipedia")
# homepage.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("python", Keys.ENTER)
