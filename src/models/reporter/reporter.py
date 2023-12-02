from pathlib import Path

class Reporter:
    __task_calculator: dict

    def __init__(self, events) -> None:
        self.__events: dict

    @classmethod
    def from_path(cls, origin_path: Path) -> None:
        pass
    
    def move_files(target_path: Path) -> None:
        pass