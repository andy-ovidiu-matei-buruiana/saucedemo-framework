from testdata.items import ITEMS

def test_remove_from_cart(logged_in_inventory):
    # add item to cart
    logged_in_inventory.add_to_cart(ITEMS[0])
    # verify cart was updated
    count = logged_in_inventory.cart_badge_count()
    assert count == 1

    # remove the added item from cart
    logged_in_inventory.remove_from_cart(ITEMS[0])

    # ! check cart is empty
    logged_in_inventory.cart_is_empty()

    # logout
    logged_in_inventory.logout()

