from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage


class Header(BasePage):
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_URL = "/cart.html"
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-test='checkout']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    ALL_ITEMS_LINK = (By.ID, "inventory-sidebar-link")

    def is_loaded(self) -> None:
        self._wait_visible(self.CART_LINK)

    def logout(self) -> None:
        self._click(self.MENU_BTN)
        self._click(self.LOGOUT_LINK)

    def go_to_cart(self) -> CartPage:
        self._click(self.CART_LINK)
        return CartPage(self.driver, self.timeout)

    def cart_badge_count(self) -> int:
        badge = self._wait_visible(self.CART_BADGE)
        return int(badge.text)

    def cart_is_empty(self) -> None:
        self._wait_invisible(self.CART_BADGE)

    def go_to_all_items(self):
        self._click(self.MENU_BTN)
        self._click(self.ALL_ITEMS_LINK)

        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver, self.timeout)
