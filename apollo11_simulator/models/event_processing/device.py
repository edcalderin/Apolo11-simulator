from pydantic import BaseModel, ConfigDict

from apollo11_simulator.models.event_processing.device_status import DeviceStatus


class Device(BaseModel):
    """Device class that inherits from Pydantic BaseModel.

    Args:
        device_type (str): Name of device
        device_status (DeviceStatus | str): Status of DeviceStatus type
        device_description (str): Description of the device
    """

    model_config = ConfigDict(use_enum_values=True)
    device_type: str
    device_status: DeviceStatus
    device_description: str
