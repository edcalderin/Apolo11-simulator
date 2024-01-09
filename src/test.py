from src.models.event_processing.orbit_one import OrbitOne
from src.models.event_processing.service_type import ServiceType
from src.models.event_processing.device import Device
from src.models.event_processing.device_status import DeviceStatus
from src.models.event_processing.unkn import Unkn

from datetime import datetime


orbit_one = OrbitOne(
    date=datetime.now(), 
    budget= 2,
    satellite_name='OpenAI',
    service_type= ServiceType.UPDATE,
    device = Device(device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)
)
orbit_one.generate_event()

unkn = Unkn(uuid='1', date=datetime.now(), budget='unknown', device=Device(device_type='unknown', device_status=DeviceStatus.UNKNOWN, device_age='unknown'))
unkn.generate_event()