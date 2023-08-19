from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

event_time = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
event_name = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')

events = {}

for x in range(0, len(event_time)):
    events[x] = {
        "time": event_time[x].text,
        "name": event_name[x].text
    }

print(events)
