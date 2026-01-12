import pytest
from flows.login_flow import LoginFlow
from models.login_user import LogInUserInfo
from testdata.users import VALID_USERS, INVALID_USERS, PASSWORD

ERROR_TEXT = "Epic sadface: Sorry, this user has been locked out."

@pytest.mark.parametrize("uname", VALID_USERS)
def test_valid_login(browser, uname):
    user = LogInUserInfo(uname, PASSWORD)
    inventory = LoginFlow.login_successful(browser, 10, user)

    inventory.is_loaded()
    inventory.header.logout()


@pytest.mark.parametrize("uname", INVALID_USERS)
def test_invalid_login(browser, uname):
    user = LogInUserInfo(uname, PASSWORD)
    LoginFlow.login_unsuccessful(browser, 10, user, ERROR_TEXT)
