import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from testdata.users import VALID_USERS, PASSWORD


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_inventory(browser):
    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()
    # login with valid user
    inventory_page = login.login(VALID_USERS[0], PASSWORD)
    # verify login successful
    inventory_page.is_loaded()

    return inventory_page