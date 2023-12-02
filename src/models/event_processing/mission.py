from device import Device
from typing import List

class Mission:
    def __init__(self, start_date, end_date, budget: float, devices: List[Device]) -> None:
        self.__start_date = start_date
        self.__end_date = end_date
        self.__budget = budget
        self.__devices = devices

    @property
    def duration(self):
        return self.__end_date - self.__start_date

    def generate_event(self)->None:
        raise NotImplementedError()