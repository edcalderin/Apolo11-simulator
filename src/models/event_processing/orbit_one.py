from mission import Mission
from service_type import ServiceType

class OrbitOne(Mission):
    def __init__(self, satellite_name:str, service_type: ServiceType) -> None:
        self.__satellite_name = satellite_name
        self.__service_type = service_type