from testdata.items import ITEMS

def test_remove_from_cart(inventory_page):
    # add item to cart
    inventory_page.add_to_cart(ITEMS[0])
    # verify cart was updated
    count = inventory_page.header.cart_badge_count()
    assert count == 1

    # remove the added item from cart
    inventory_page.remove_from_cart(ITEMS[0])

    # ! check cart is empty
    inventory_page.header.cart_is_empty()

    # logout
    inventory_page.header.logout()

