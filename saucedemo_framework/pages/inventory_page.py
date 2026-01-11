from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from pages.cart_page import CartPage


class InventoryPage(BasePage):
    CART_URL = "cart.html"
    INVENTORY_URL_PART = "inventory.html"
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ACTIVE_SORT = (By.CSS_SELECTOR, "[data-test='active-option']")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    INVENTORY_PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    INVENTORY_NAMES = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")

    def is_loaded(self) -> None:
        self._wait_visible(self.CART_LINK)
        self._wait_url_contains(self.INVENTORY_URL_PART)

    def logout(self) -> None:
        self._click(self.MENU_BTN)
        self._click(self.LOGOUT_LINK)

    def add_to_cart(self, item: str) -> None:
        add_button_id = "add-to-cart-" + item.lower().replace(" ", "-")
        self._click((By.ID, add_button_id))

    def remove_from_cart(self, item: str) -> None:
        remove_button_id = "remove-" + item.lower().replace(" ", "-")
        self._click((By.ID, remove_button_id))

    def cart_badge_count(self) -> int:
        badge = self._wait_visible(self.CART_BADGE)
        return int(badge.text)

    def cart_is_empty(self) -> None:
        self._wait_invisible(self.CART_BADGE)

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

    def go_to_cart(self) -> CartPage:
        self._click(self.CART_LINK)
        self._wait_url_contains(self.CART_URL)
        self._wait_clickable(self.CHECKOUT_BTN)
        return CartPage(self.driver, self.timeout)