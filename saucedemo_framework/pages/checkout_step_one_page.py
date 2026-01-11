from typing import Optional
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_step_two_page import CheckoutStepTwoPage


class CheckoutStepOnePage(BasePage):
    CHECKOUT_S1_URL = "checkout-step-one"
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-test='continue']")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_info(self, fname: str, lname: str, zcode: str) -> CheckoutStepTwoPage:
        self._wait_url_contains(self.CHECKOUT_S1_URL)
        self._type(self.FIRST_NAME, fname)
        self._type(self.LAST_NAME, lname)
        self._type(self.ZIP_CODE, zcode)
        self._click(self.CONTINUE_BTN)

        return CheckoutStepTwoPage(self.driver, self.timeout)

    def fill_wrong_info(self, fname: Optional[str] = None, lname: Optional[str] = None, zcode: Optional[str] = None) -> str:
        self._wait_url_contains(self.CHECKOUT_S1_URL)

        if not fname is None:
            self._type(self.FIRST_NAME, fname)
        if not lname is None:
            self._type(self.LAST_NAME, lname)
        if not zcode is None:
            self._type(self.ZIP_CODE, zcode)
        self._click(self.CONTINUE_BTN)

        return self._text(self.ERROR)

