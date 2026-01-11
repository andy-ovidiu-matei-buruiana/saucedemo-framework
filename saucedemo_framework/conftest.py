import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from testdata.users import VALID_USERS, PASSWORD


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()

    # Disable password manager + credential prompts
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    # reduce random Chrome UI interruptions
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    # use guest to remove password leak prompts
    options.add_argument("--guest")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.switch_to.window(driver.current_window_handle)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_inventory(browser: WebDriver) -> InventoryPage:
    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()
    # login with valid user
    inventory_page = login.login(VALID_USERS[0], PASSWORD)
    # verify login successful
    inventory_page.is_loaded()

    return inventory_page