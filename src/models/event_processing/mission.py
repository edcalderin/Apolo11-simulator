from src.models.event_processing.device import Device
from typing import List
from pydantic import BaseModel, computed_field
import yaml
from datetime import datetime

class Mission(BaseModel):
    start_date: datetime
    end_date: datetime
    budget: float
    devices: List[Device]

    @computed_field
    @property
    def duration(self)->int:
        return (self.end_date - self.start_date).days

    def generate_event(self, name:str) -> None:
        with open(name, 'w+') as file:
            yaml.dump(self.model_dump(), file)