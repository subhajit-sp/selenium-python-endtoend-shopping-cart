import profile

import pytest
from selenium import webdriver
#from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

import time

@pytest.fixture(scope='module')
def browser_init(request):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-popup-blocking')
    #options.add_experimental_option('prefs', {"profile.password_manager_enabled": False,
    #                                          "profile.credentials_enable_service": False,
    #                                          "profile.password_manager_leak_detection": False
    #                                          })
    driver = webdriver.Chrome(options = options)
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_sample(browser_init):
    driver = browser_init
    driver.get("https://www.makemytrip.com")
    driver.find_element(By.XPATH, "//span[@class = 'commonModal__close']").click()
    driver.find_element(By.XPATH, "//input[contains(@class, 'react-autosuggest__')]").send_keys("Kol")


    time.sleep(5)


