import time
from selenium import webdriver
from cookie_clicker import Cookie_Clicker, Store

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie_clicker = Cookie_Clicker(driver)
store = Store(driver)

# timings
game_time = time.time() + 60 * 5
five_sec_timer = time.time() + 5

while True:
    # clicking the cookies
    cookie_clicker.cookie.click()
    if time.time() > five_sec_timer:
        # getting all items from the store
        store.get_all_store_element()
        # clicking the target element
        store.target_element()
        # resetting the five second's timer
        five_sec_timer = time.time() + 5

    if time.time() > game_time:
        # if present time is over than the game time
        # cookies per second
        cookies_per_second = cookie_clicker.ratio()
        print(cookies_per_second)
        break
