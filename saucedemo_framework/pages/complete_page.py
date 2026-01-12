from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CompletePage(BasePage):
    ORDER_COMPLETE = (By.CSS_SELECTOR, "[data-test='complete-header']")
    FINISH_MSG = "Thank you for your order!"
    HOME_BTN = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    CHECKOUT_COMPLETE_URL = "checkout-complete"
    URL_PART = "/checkout-complete.html"

    def is_loaded(self) -> None:
        self._wait_url_contains(self.URL_PART)

    def back_home(self):
        self._wait_url_contains(self.CHECKOUT_COMPLETE_URL)
        self._wait_text_present(self.ORDER_COMPLETE, self.FINISH_MSG)
        self._click(self.HOME_BTN)

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver, self.timeout)