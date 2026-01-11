import pytest

from testdata.items import ITEMS
from testdata.user_information import INFORMATION_COMBINATION


@pytest.mark.parametrize("fname, lname, zcode, error_text", INFORMATION_COMBINATION)
def test_checkout(logged_in_inventory, fname, lname, zcode, error_text):
    logged_in_inventory.add_to_cart(ITEMS[0])
    checkout = logged_in_inventory.go_to_cart()
    step_one = checkout.checkout()

    error = step_one.fill_wrong_info(fname, lname, zcode)

    assert error.text.strip() == error_text



