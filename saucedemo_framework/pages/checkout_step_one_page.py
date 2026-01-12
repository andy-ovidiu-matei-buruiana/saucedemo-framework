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
    URL_PART = "/checkout-step-one.html"

    def is_loaded(self) -> None:
        self._wait_url_contains(self.URL_PART)

    def submit_info(
            self,
            fname: Optional[str] = None,
            lname: Optional[str] = None,
            zcode: Optional[str] = None
        ) -> Optional[CheckoutStepTwoPage]:

        self._wait_url_contains(self.CHECKOUT_S1_URL)
        if fname is not None:
            self._type(self.FIRST_NAME, fname)
        if lname is not None:
            self._type(self.LAST_NAME, lname)
        if zcode is not None:
            self._type(self.ZIP_CODE, zcode)

        self._click(self.CONTINUE_BTN)

        if self._is_visible(self.ERROR):
            return None

        return CheckoutStepTwoPage(self.driver, self.timeout)

    def error_text(self) -> str:
        return self._text(self.ERROR)
