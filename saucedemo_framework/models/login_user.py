from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class LogInUserInfo:
    username: Optional[str]
    password: Optional[str]