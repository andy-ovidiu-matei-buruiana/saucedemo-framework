import pytest
from testdata.items import ITEMS

@pytest.mark.parametrize("item", ITEMS)
def test_add_to_cart(inventory_page, item):
    # add item to cart
    inventory_page.add_to_cart(item)

    # assess count
    count = inventory_page.header.cart_badge_count()
    assert count == 1

    inventory_page.header.logout()

