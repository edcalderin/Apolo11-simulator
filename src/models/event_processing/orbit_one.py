from mission import Mission
from service_type import ServiceType
from pydantic import BaseModel

class OrbitOne(Mission, BaseModel):
    satellite_name: str
    service_type: ServiceType