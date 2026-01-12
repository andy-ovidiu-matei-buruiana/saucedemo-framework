import pytest

from flows.checkout_flow import CheckoutFlow
from models.checkout_user import UserInfo
from testdata.items import ITEMS

@pytest.mark.parametrize("item", ITEMS)
def test_checkout_success(inventory_page, item):
    info = UserInfo("Test", "User", "1234")
    inventory = CheckoutFlow.checkout_one_item_success(inventory_page, item, info)

    inventory.is_loaded()
