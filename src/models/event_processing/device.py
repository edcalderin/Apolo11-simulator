from device_status import DeviceStatus

class Device:
    def __init__(self, id: str, device_type: str, device_status: DeviceStatus, device_age: int) -> None:
        self.id = id
        self.device_type = device_type
        self.device_status = device_status
        self.device_age = device_age

    def get_hash(self, mission_name: str) -> str:
        pass