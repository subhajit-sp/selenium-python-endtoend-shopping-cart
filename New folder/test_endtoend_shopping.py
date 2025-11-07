from selenium import webdriver
from PageObject.ProductPage import ProductPage
from test_data import TestData
from PageObject.CartPage import CartPage
from PageObject.CheckOut import Checkout
import time
import logging

LOG_FILENAME = 'Log.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO, force=True)
logging.info("Logger initialized")

def test_shopping(browser_init):
    driver = browser_init
    product_page = ProductPage(driver)
    logging.info("Opening shopping cart")
    cart_items = product_page.product_page(TestData.base_url, TestData.user_input[0], TestData.page_title)
    logging.info("Added Items in cart and checkout")

    place_order = CartPage(driver)
    place_order.place_order(cart_items, TestData.user_input[1], TestData.user_input[2])
    logging.info("Verified and card items and discount")

    checkout = Checkout(driver)
    checkout.final_checkout(TestData.user_input[3])
    logging.info("Completed purchase")

    driver.get_screenshot_as_file("new.png")



