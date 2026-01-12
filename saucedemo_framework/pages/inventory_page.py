from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from components.header import Header
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_URL_PART = "/inventory.html"
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ACTIVE_SORT = (By.CSS_SELECTOR, "[data-test='active-option']")
    INVENTORY_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    INVENTORY_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def __init__(self, driver: WebDriver, timeout: int) -> None:
        super().__init__(driver, timeout)
        self.header = Header(driver, timeout)

    def is_loaded(self) -> None:
        self.header.is_loaded()
        self._wait_url_contains(self.INVENTORY_URL_PART)

    def add_to_cart(self, item: str) -> None:
        add_button_id = "add-to-cart-" + item.lower().replace(" ", "-")
        self._click((By.ID, add_button_id))

    def remove_from_cart(self, item: str) -> None:
        remove_button_id = "remove-" + item.lower().replace(" ", "-")
        self._click((By.ID, remove_button_id))

    def sort(self, sorting: str) -> None:
        dropdown = self._wait_clickable(self.SORT_DROPDOWN)
        Select(dropdown).select_by_visible_text(sorting)

        # * is for unpacking tuple
        self.wait.until(
            lambda d: d.find_element(*self.ACTIVE_SORT).text.strip() == sorting
        )

    def get_prices(self) -> List[float]:
        prices = self._find_all(self.INVENTORY_PRICES)
        return [float(price.text.strip("$")) for price in prices]

    def get_item_names(self) -> List[str]:
        names = self._find_all(self.INVENTORY_NAMES)
        return [name.text.strip() for name in names]
