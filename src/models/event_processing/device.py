from src.models.event_processing.device_status import DeviceStatus
from pydantic import ConfigDict
import hashlib
from pydantic import BaseModel

class Device(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    id: int
    device_type: str
    device_status: DeviceStatus
    device_age: int

    def get_hash(self, mission_date: str, mission_name: str) -> str:
        hash = hashlib.sha256()
        hash.update(mission_date.encode())
        hash.update(mission_name.encode())
        hash.update(self.device_type.encode())
        hash.update(self.device_status.value.encode())
        return hash.hexdigest()

