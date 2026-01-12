from typing import Optional

from models.checkout_user import UserInfo
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.complete_page import CompletePage
from pages.inventory_page import InventoryPage


class CheckoutFlow:

    @staticmethod
    def start_checkout(inventory: InventoryPage, item: str) -> CheckoutStepOnePage:
        inventory.add_to_cart(item)

        checkout = inventory.header.go_to_cart()
        checkout.is_loaded()

        step_one = checkout.checkout()
        step_one.is_loaded()

        return step_one

    @staticmethod
    def submit_info(step_one: CheckoutStepOnePage, info: UserInfo) -> Optional[CheckoutStepTwoPage]:
        step_two = step_one.submit_info(info.first_name, info.last_name, info.zip_code)

        if step_two is not None:
            step_two.is_loaded()

        return step_two

    @staticmethod
    def finish(step_two: CheckoutStepTwoPage) -> CompletePage:
        complete = step_two.finish()
        complete.is_loaded()

        return complete

    @staticmethod
    def checkout_one_item_success(inventory: InventoryPage, item: str, info: UserInfo) -> InventoryPage:
        step_one = CheckoutFlow.start_checkout(inventory, item)
        step_two = CheckoutFlow.submit_info(step_one, info)
        complete = CheckoutFlow.finish(step_two) # type: ignore

        assert step_two is not None, f"Expected checkout to succeed but got error: {step_one.error_text()}"
        return complete.back_home() # type: ignore

    @staticmethod
    def checkout_expect_error(inventory: InventoryPage, item: str, info: UserInfo) -> str:
        step_one = CheckoutFlow.start_checkout(inventory, item)
        step_two = CheckoutFlow.submit_info(step_one, info)

        assert step_two is None, "Expected validation error, but checkout continued to step two."
        return step_one.error_text()