from typing import Any, Tuple

class EventGenerator:
    def __init__(self, frequency_seconds: int, number_of_files: Tuple[int, int]) -> None:
        self.frequency_seconds = frequency_seconds
        self.number_of_files = number_of_files

    def __call__(self) -> Any:
        pass