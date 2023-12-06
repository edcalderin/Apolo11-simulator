from src.models.event_processing.orbit_one import OrbitOne
from src.models.event_processing.service_type import ServiceType
from src.models.event_processing.device  import Device
from src.models.event_processing.device_status import DeviceStatus

orbit_one = OrbitOne(start_date='d', 
    end_date = 'a',
    budget= 2,
    devices= [Device(id=2, device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)],
    satellite_name='OpenAI',
    service_type= ServiceType.UPDATE
    )

orbit_one.generate_event()