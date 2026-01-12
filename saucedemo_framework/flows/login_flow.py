from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver

from models.login_user import LogInUserInfo
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class LoginFlow:

    @staticmethod
    def open_login_page(browser: WebDriver, timeout: int) -> LoginPage:
        login = LoginPage(browser, timeout)
        login.open()
        login.is_loaded()

        return login


    @staticmethod
    def finish_login(login: LoginPage, user: LogInUserInfo) -> Optional[InventoryPage]:
        inventory = login.login(user.username, user.password)
        return inventory

    @staticmethod
    def login_successful(browser: WebDriver, timeout: int, user: LogInUserInfo) -> InventoryPage:
        login = LoginFlow.open_login_page(browser, timeout)
        inventory = LoginFlow.finish_login(login, user)

        assert inventory is not None, f"Expected login but error appeared: {login.error_text()}"
        return inventory

    @staticmethod
    def login_unsuccessful(browser: WebDriver, timeout: int, user: LogInUserInfo, error: str) -> None:
        login = LoginFlow.open_login_page(browser, timeout)
        inventory = LoginFlow.finish_login(login, user)

        assert inventory is None, "Expected error but login went through"
        assert login.error_text_present(error)
