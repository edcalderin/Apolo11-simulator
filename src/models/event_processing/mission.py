from device import Device
from typing import List
from pydantic import BaseModel, computed_field
import yaml

class Mission(BaseModel):
    start_date: str
    end_date: str
    budget: float
    devices: List[Device]

    @computed_field
    @property
    def duration(self)->str:
        return ''.join([self.end_date, self.start_date])

    def generate_event(self, name:str) -> None:
        with open(name, 'w') as file:
            yaml.dump(self.model_dump(), file)