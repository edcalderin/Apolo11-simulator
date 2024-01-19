from apollo11_simulator.models.event_processing.device_status import DeviceStatus
from pydantic import ConfigDict
from pydantic import BaseModel

class Device(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    device_type: str
    device_status: DeviceStatus | str
    device_age: int | str
    device_description: str
    