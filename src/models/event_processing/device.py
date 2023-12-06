from device_status import DeviceStatus
from pydantic import BaseModel, ConfigDict

class Device(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    id: str
    device_type: str
    device_status: DeviceStatus
    device_age: int
    
    def get_hash(self, mission_name: str) -> str:
        pass
    
 