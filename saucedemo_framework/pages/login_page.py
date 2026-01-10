from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    LOGIN_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        self._wait_visible(self.USERNAME)
        self._wait_visible(self.PASSWORD)
        self._wait_visible(self.LOGIN_BTN)

    def login(self, uname, pword):
        self._wait_visible(self.USERNAME).send_keys(uname)
        self._wait_visible(self.PASSWORD).send_keys(pword)
        self._click(self.LOGIN_BTN)

        return InventoryPage(self.driver, self.timeout)

    def login_failed(self, text):
        return self._wait_text_present(self.LOGIN_ERROR, text)