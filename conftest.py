import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run in headless mode")
    parser.addoption("--browser", action="store_true", default=False, help="Run in browser mode")


@pytest.fixture(params=['chrome', 'firefox', 'Edge'], scope='function')
def browser_init(request):
    browser = request.param
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--browser")
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    elif browser == 'Edge':
        driver = webdriver.Edge()

    driver.set_page_load_timeout(5)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
