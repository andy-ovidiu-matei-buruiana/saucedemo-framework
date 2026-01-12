from typing import Optional
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    INVENTORY_URL_PART = "/inventory.html"

    def open(self) -> None:
        self.driver.get(self.URL)

    def is_loaded(self) -> None:
        self._wait_visible(self.USERNAME)
        self._wait_visible(self.PASSWORD)
        self._wait_visible(self.LOGIN_BTN)

    def login(self, uname: str, pword: str) -> Optional[InventoryPage]:
        self._type(self.USERNAME, uname)
        self._type(self.PASSWORD, pword)
        self._click(self.LOGIN_BTN)

        # Wait for either: error shows OR inventory URL happens
        self.wait.until(
            lambda d: self._is_visible(self.LOGIN_ERROR) or self.INVENTORY_URL_PART in d.current_url
        )

        if self._is_visible(self.LOGIN_ERROR):
            return None

        inventory = InventoryPage(self.driver, self.timeout)
        inventory.is_loaded()
        return inventory

    def error_text_present(self, text: str) -> bool:
        return self._wait_text_present(self.LOGIN_ERROR, text)

    def error_text(self) -> str:
        return self._text(self.LOGIN_ERROR)
