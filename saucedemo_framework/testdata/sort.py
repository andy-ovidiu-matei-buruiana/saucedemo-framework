from typing import Callable, List, Tuple
from pages.inventory_page import InventoryPage

SortGetter = Callable[[InventoryPage], List[float] | List[str]]
SortCase = Tuple[str, SortGetter, bool]

SORT_CASES = [
    ("Price (low to high)", lambda inv: inv.get_prices(), False),
    ("Price (high to low)", lambda inv: inv.get_prices(), True),
    ("Name (A to Z)", lambda inv: inv.get_item_names(), False),
    ("Name (Z to A)", lambda inv: inv.get_item_names(), True),
]