from orbit_one import OrbitOne
from service_type import ServiceType
from device  import Device
from device_status import DeviceStatus

orbit_one = OrbitOne(start_date='d', 
    end_date = 'a',
    budget= 2,
    devices= [Device(id='2', device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)],
    satellite_name='OpenAI',
    service_type= ServiceType.UPDATE
    )

orbit_one.generate_event()