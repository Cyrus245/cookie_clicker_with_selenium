from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cookie_Clicker:
    def __init__(self, driver):
        self.driver = driver
        self.cookie = self.get_cookie()
        self.cookie_count = self.count_cookie()
        # self.items_ids = self.get_item_ids()

    def get_cookie(self):
        """This method will find the cookie """
        return self.driver.find_element(By.ID, "cookie")

    def count_cookie(self):
        """This method returns the cookie count"""
        return self.driver.find_element(By.XPATH, '//*[@id="money"]')

    def ratio(self):
        """This method will find the cookie ratio"""
        return self.driver.find_element(By.XPATH, '//*[@id="cps"]').text


class Store(Cookie_Clicker):
    def __init__(self, driver):
        super().__init__(driver)
        self.items_ids = self.get_item_ids()

    def get_all_store_element(self):
        """This method will get all the store element"""
        wait = WebDriverWait(self.driver, 5)
        # checking the located item is in the dom or not and wait until 5s
        all_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="store"]/div/b')))

        return all_elements

    def get_item_ids(self):
        """This method will find the store items ids"""

        # finding the price divs
        items = self.driver.find_elements(By.CSS_SELECTOR, "#store div")
        # storing the price divs ID in a list
        items_ids = [x.get_attribute('id') for x in items]
        return items_ids

    def parsing(self, arr):
        """This method will parse the price from all the store items"""
        price_list = []
        for x in arr:
            # splitting by hyphen
            split_text = x.text.split('-')
            if len(split_text) > 1:
                # removing commas and trailing spaces
                price_str = int(split_text[1].replace(',', '').strip())
                price_list.append(price_str)
        # passing the price list to check the price
        result = self.checking_the_price(price_list)

        return result

    def checking_the_price(self, price_list):
        """This method will check the most high-priced item from the store """
        maximum_list = []

        for price in price_list:
            # print(self.cookie_count)
            if price < int(self.cookie_count.text):
                maximum_list.append(price)

        if maximum_list:
            max_price = max(maximum_list)
            result = price_list.index(max_price)
            print(result)
            return result
        else:
            # Return None if no affordable item is found
            return None

    def target_element(self):
        """this method will find the targeted element and click it"""

        # checking all the element price and finding the maximum one's index
        target = self.parsing(self.get_all_store_element())

        # clicking the targeted item
        self.driver.find_element(By.ID, self.items_ids[target]).click()
