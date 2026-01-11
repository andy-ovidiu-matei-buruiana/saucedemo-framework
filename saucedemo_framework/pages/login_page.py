from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self) -> None:
        self.driver.get(self.URL)

    def is_loaded(self) -> bool:
        self._wait_visible(self.USERNAME)
        self._wait_visible(self.PASSWORD)
        self._wait_visible(self.LOGIN_BTN)

        return True

    def login(self, uname: str, pword: str) -> InventoryPage:
        self._wait_visible(self.USERNAME).send_keys(uname)
        self._wait_visible(self.PASSWORD).send_keys(pword)
        self._click(self.LOGIN_BTN)

        return InventoryPage(self.driver, self.timeout)

    def login_failed(self, text: str) -> bool:
        return self._wait_text_present(self.LOGIN_ERROR, text)