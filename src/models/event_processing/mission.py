from src.models.event_processing.device import Device
from typing import List, Optional
from pydantic import BaseModel, computed_field, Field
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

    def generate_event(self, name: str) -> None:
        model_dict = self.model_dump()
        for device in model_dict.get('devices'):
            device['hash'] = Device(**device).get_hash(str(self.start_date), self.__class__.__name__)
        with open(name, 'w+') as file:
            yaml.dump(model_dict, file)