import pytest
from testdata.sort import SORT_CASES


@pytest.mark.parametrize("sort_option, getter, reverse", SORT_CASES)
def test_sort_low_high(inventory_page, sort_option, getter, reverse):
    # sort low to high
    inventory_page.sort(sort_option)
    # get all values in a list
    values = getter(inventory_page)

    # verify values are sorted
    assert values == sorted(values, reverse=reverse)
    inventory_page.header.logout()