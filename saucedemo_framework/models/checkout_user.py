from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class UserInfo:
    first_name: Optional[str]
    last_name: Optional[str]
    zip_code: Optional[str]