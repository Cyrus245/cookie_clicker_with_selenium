import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# finding the cookie
cookie = driver.find_element(By.ID, "cookie")

# current cookie count
cookie_count = driver.find_element(By.XPATH, '//*[@id="money"]')

# timings
game_time = time.time() + 60 * 1
five_sec_timer = time.time() + 5

# finding the price divs
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# storing the price divs ID in a list
items_ids = [x.get_attribute('id') for x in items]


def checking_the_price(price_list):
    maximum_list = []
    for price in price_list:
        if price < int(cookie_count.text):
            maximum_list.append(price)

    if maximum_list:
        max_price = max(maximum_list)
        result = price_list.index(max_price)
        return result
    else:
        # Return None if no affordable item is found
        return None


def checking_and_parsing(arr):
    price_list = []
    for x in arr:
        # splitting by hyphen
        split_text = x.text.split('-')
        if len(split_text) > 1:
            # removing commas and trailing spaces
            price_str = int(split_text[1].replace(',', '').strip())
            price_list.append(price_str)
    # passing the price list to check the price
    result = checking_the_price(price_list)

    return result


while True:
    # clicking the cookies
    cookie.click()
    if time.time() > five_sec_timer:
        wait = WebDriverWait(driver, 5)
        # checking the located item is in the dom or not and wait until 5s
        all_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="store"]/div/b')))

        # checking all the element price and finding the maximum one's index
        target = checking_and_parsing(all_elements)

        # clicking the targeted item
        driver.find_element(By.ID, items_ids[target]).click()

        # resetting the five second's timer
        five_sec_timer = time.time() + 5

    if time.time() > game_time:
        # if present time is over than the game time
        # cookies per second
        cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cps"]').text
        print(cookies_per_second)
        break
