import pytest
from flows.login_flow import LoginFlow
from models.login_user import LogInUserInfo
from testdata.users import VALID_USERS, INVALID_USERS, PASSWORD

ERROR_TEXT = "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.parametrize("uname", VALID_USERS)
def test_valid_login(browser, timeout, uname):
    user = LogInUserInfo(uname, PASSWORD)
    inventory = LoginFlow.login_successful(browser, timeout, user)

    inventory.is_loaded()
    inventory.header.logout()


@pytest.mark.parametrize("uname", INVALID_USERS)
def test_invalid_login(browser, timeout, uname):
    user = LogInUserInfo(uname, PASSWORD)
    LoginFlow.login_unsuccessful(browser, timeout, user, ERROR_TEXT)
