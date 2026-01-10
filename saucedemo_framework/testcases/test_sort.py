import pytest
from testdata.sort import SORT_CASES


@pytest.mark.parametrize("sort_option, getter, reverse", SORT_CASES)
def test_sort_low_high(logged_in_inventory, sort_option, getter, reverse):
    # sort low to high
    logged_in_inventory.sort(sort_option)
    # get all values in a list
    values = getter(logged_in_inventory)

    # verify values are sorted
    assert values == sorted(values, reverse=reverse)
    logged_in_inventory.logout()