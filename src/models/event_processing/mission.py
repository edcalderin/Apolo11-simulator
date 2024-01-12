from src.models.event_processing.device import Device
from pydantic import BaseModel, computed_field
import yaml
from datetime import datetime
import hashlib

class Mission(BaseModel):
    date: datetime
    budget: float | str
    device: Device
    
    @computed_field
    @property
    def mission(self)-> str:
        return self.__class__.__name__
    
    @computed_field
    @property
    def hash(self) -> str:
        hash = hashlib.sha256()
        hash.update(str(self.date).encode())
        hash.update(self.mission.encode())
        hash.update(self.device.device_type.encode())
        hash.update(self.device.device_status.encode())
        return hash.hexdigest()

    def __str__(self) -> str:
        return 'APL'
    
    def generate_event(self, name: str) -> None:
        with open(name, 'w+') as file:
            yaml.dump(self.model_dump(), file)