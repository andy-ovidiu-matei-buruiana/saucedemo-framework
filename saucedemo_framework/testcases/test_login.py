import pytest
from pages.login_page import LoginPage
from testdata.users import VALID_USERS, INVALID_USERS, PASSWORD

ERROR_TEXT = "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.parametrize("uname", VALID_USERS)
def test_valid_login(browser, uname):

    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()
    # login with each user
    inventory_page = login.login(uname, PASSWORD)

    # * Verify login successful
    inventory_page.is_loaded()

    inventory_page.logout()

@pytest.mark.parametrize("uname", INVALID_USERS)
def test_invalid_login(browser, uname):
    # create Login Page object
    login = LoginPage(browser, 10)
    # open page
    login.open()
    # login with each user
    login.login(uname, PASSWORD)

    # * Verify login not successful
    login.login_failed(ERROR_TEXT)
