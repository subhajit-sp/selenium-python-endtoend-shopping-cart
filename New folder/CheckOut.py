from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class Checkout:
    #locator]
    CHECK_BOX = (By.XPATH, "//input[@type = 'checkbox']")
    SUBMIT = (By.XPATH, "//button[contains(text(), 'Proceed')]")
    SELECT_BOX = (By.XPATH, "//div[@class='wrapperTwo']//div//select")

    def __init__(self, driver):
        self.driver = driver

    def final_checkout(self, country):
        option = Select(self.driver.find_element(*self.SELECT_BOX))
        option.select_by_visible_text(country)
        self.driver.find_element(*self.CHECK_BOX).click()
        self.driver.find_element(*self.SUBMIT).click()
