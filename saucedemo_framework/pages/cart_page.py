from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from components.header import Header
from pages.base_page import BasePage
from pages.checkout_step_one_page import CheckoutStepOnePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")
    URL_PART = "/cart.html"

    def __init__(self, driver: WebDriver, timeout: int) -> None:
        super().__init__(driver, timeout)
        self.header = Header(driver, timeout)

    def is_loaded(self) -> None:
        self._wait_url_contains(self.URL_PART)
        self._wait_clickable(self.CHECKOUT_BTN)

    def checkout(self) -> CheckoutStepOnePage:
        self._click(self.CHECKOUT_BTN)
        return CheckoutStepOnePage(self.driver, self.timeout)
