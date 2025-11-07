from tkinter import Place

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.CartPage import CartPage


class ProductPage:
    #locator
    SEARCH_B0X = (By.XPATH, "//input[@type = 'search']")
    ITEM_LIST = (By.XPATH, "//div[@class='product']")
    ADDTOCART = (By.XPATH, ".//div[@class = 'product-action']/button")
    PRODUCT_NAME = (By.XPATH, ".//h4[@class='product-name']")
    CART = (By.CSS_SELECTOR, "a.cart-icon")
    CHECKOUT = (By.XPATH, "//button[contains(text(), 'PROCEED TO CHECKOUT')]")


    def __init__(self, driver):
        self.driver = driver

    def product_page(self, base_url, user_input, heading):
        """Select product add to cart"""
        selected_product_list = []
        self.driver.get(base_url)
        assert self.driver.title == heading, "Incorrect Page Loaded"
        self.driver.find_element(*self.SEARCH_B0X).send_keys(user_input)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_all_elements_located(self.ITEM_LIST))
        products =  self.driver.find_elements(*self.ITEM_LIST)
        assert len(products) > 0, "No Products Found"
        for product in products:
            selected_product_list.append(product.find_element(*self.PRODUCT_NAME).text)
            product.find_element(*self.ADDTOCART).click()
        self.driver.find_element(*self.CART).click()
        self.driver.find_element(*self.CHECKOUT).click()
        return selected_product_list












