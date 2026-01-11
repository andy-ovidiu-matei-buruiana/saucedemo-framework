from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.complete_page import CompletePage


class CheckoutStepTwoPage(BasePage):
    CHECKOUT_S2_URL = "checkout-step-two"
    FINISH_BTN = (By.CSS_SELECTOR, "[data-test='finish']")

    def finish(self) -> CompletePage:
        self._wait_url_contains(self.CHECKOUT_S2_URL)
        self._click(self.FINISH_BTN)

        return CompletePage(self.driver, self.timeout)