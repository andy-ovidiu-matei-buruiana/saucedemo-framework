from testdata.items import ITEMS

def test_checkout(logged_in_inventory):
    logged_in_inventory.add_to_cart(ITEMS[0])
    checkout = logged_in_inventory.go_to_cart()

    step_one = checkout.checkout()

    step_two = step_one.fill_info("Test", "User", "1234")

    complete = step_two.finish()

    complete.back_home()

    logged_in_inventory.is_loaded()
