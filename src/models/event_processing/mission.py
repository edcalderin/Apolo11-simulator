from device import Device
from typing import List
from pydantic import BaseModel, computed_field

class Mission(BaseModel):
    start_date: str
    end_date: str
    budget: float
    devices: List[Device]

    @computed_field
    @property
    def duration(self):
        return self.end_date - self.start_date

    def generate_event(self) -> None:
        raise NotImplementedError()