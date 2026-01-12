import pytest

from flows.checkout_flow import CheckoutFlow
from models.checkout_user import UserInfo
from testdata.items import ITEMS
from testdata.user_information import INFORMATION_COMBINATION


@pytest.mark.parametrize("fname, lname, zcode, error_text", INFORMATION_COMBINATION)
def test_checkout(inventory_page, fname, lname, zcode, error_text):
    info = UserInfo(fname, lname, zcode)
    error = CheckoutFlow.checkout_expect_error(inventory_page, ITEMS[0], info)
    assert error == error_text

