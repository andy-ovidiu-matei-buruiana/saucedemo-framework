from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout_step_one_page import CheckoutStepOnePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")

    def checkout(self) -> CheckoutStepOnePage:
        self._click(self.CHECKOUT_BTN)
        return CheckoutStepOnePage(self.driver, self.timeout)
