from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:

    #locator
    MSG = (By.XPATH, "//span[@class = 'promoInfo']")
    PROMO_BUTTON = (By.XPATH, "//button[@class = 'promoBtn']")
    PROMO_CODE = (By.XPATH, "//input[@class = 'promoCode']")
    PRODUCTS = (By.XPATH, "//td/p[@class = 'product-name']")
    ITEMS = (By.XPATH, "//b[contains(text(), 'No. of Items')]")
    TOTAL = (By.XPATH, "//span[@class = 'totAmt']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Place Order')]")
    FINAL_AMOUNT = (By.XPATH, "//span[@class = 'discountAmt']")

    def __init__(self, driver):
        self.driver = driver

    def place_order(self, cart_items, invalid_promo, valid_promo):
        """Verifying the cart, discount etc"""
        products = self.driver.find_elements(*self.PRODUCTS)
        assert len(products) == len(cart_items), "Incorrect number of products are added in cart"
        for product in products:
            if product.text in cart_items:
                continue
            else:
                raise AssertionError (f"Incorrect cart item {product.text}")
        self.driver.find_element(*self.PROMO_CODE).send_keys(invalid_promo)
        self.driver.find_element(*self.PROMO_BUTTON).click()
        wait = WebDriverWait(self.driver, 10)
        msg = wait.until(EC.visibility_of_element_located(self.MSG))
        assert msg.text == 'Invalid code ..!', f"promo code {invalid_promo} should not be applied"
        self.driver.find_element(*self.PROMO_CODE).clear()
        self.driver.find_element(*self.PROMO_CODE).send_keys(valid_promo)
        self.driver.find_element(*self.PROMO_BUTTON).click()
        #time.sleep(10)
        wait.until(lambda d: d.find_element(*self.MSG).text != 'Invalid code ..!')
        msg = wait.until(EC.visibility_of_element_located(self.MSG))
        assert msg.text == 'Code applied ..!', f"promo code {valid_promo} should be valid and applied : {msg.text}"
        total_amount = self.driver.find_element(*self.TOTAL).text
        amount_after_discount = self.driver.find_element(*self.FINAL_AMOUNT).text
        assert total_amount > amount_after_discount, "Discount is not applied"
        self.driver.find_element(*self.SUBMIT_BUTTON).click()







