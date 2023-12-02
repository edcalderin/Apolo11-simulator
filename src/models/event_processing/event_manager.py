from typing import Any, Tuple

class EventManager:
    def __init__(self, frequency_seconds: int, number_of_files: Tuple[int, int]) -> None:
        self.__frequency_seconds = frequency_seconds
        self.__number_of_files = number_of_files

    def __call__(self) -> Any:
        pass