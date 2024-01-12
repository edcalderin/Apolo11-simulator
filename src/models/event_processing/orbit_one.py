from pydantic import ConfigDict
from src.models.event_processing.mission import Mission
from src.models.event_processing.service_type import ServiceType

class OrbitOne(Mission):
    model_config = ConfigDict(use_enum_values=True)
    satellite_name: str
    service_type: ServiceType
    
    def generate_event(self) -> None:
        name: str = f'APLORBONE-0001.log'
        super().generate_event(name)