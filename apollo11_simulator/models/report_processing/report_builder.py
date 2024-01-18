from pathlib import Path
from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator

class ReportBuilder:
    __task_calculator: TaskCalculator

    def __init__(self, events) -> None:
        self.__events: dict

    @classmethod
    def from_path(cls, origin_path: Path) -> None:
        pass

    def move_files(self, target_path: Path) -> None:
        pass
    
    def show_report():
        pass