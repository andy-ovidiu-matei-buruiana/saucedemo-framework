import pytest
from testdata.items import ITEMS

@pytest.mark.parametrize("item", ITEMS)
def test_add_to_cart(logged_in_inventory, item):
    # add item to cart
    logged_in_inventory.add_to_cart(item)

    # assess count
    count = logged_in_inventory.cart_badge_count()
    assert count == 1

    logged_in_inventory.logout()

