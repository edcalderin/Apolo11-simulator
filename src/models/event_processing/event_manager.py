from typing import Any, Tuple
from pydantic import BaseModel

class EventManager(BaseModel):
    frequency_seconds: int
    number_of_files: Tuple[int, int]

    def __call__(self) -> Any:
        pass