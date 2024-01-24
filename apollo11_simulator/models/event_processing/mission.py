import uuid
from apollo11_simulator.models.event_processing.device import Device
from pydantic import BaseModel, ConfigDict, computed_field
import yaml
from datetime import datetime
import hashlib

from apollo11_simulator.models.event_processing.service_type import ServiceType

class Mission(BaseModel):
    date: datetime
    budget: float | str
    device: Device

    @computed_field
    @property
    def mission(self) -> str:
        return self.__class__.__name__

    @computed_field
    @property
    def hash(self) -> str:
        hash = hashlib.sha256()
        hash.update(str(self.date).encode())
        hash.update(self.mission.encode())
        hash.update(self.device.device_type.encode())
        hash.update(self.device.device_status.encode())
        return hash.hexdigest()

    def __str__(self) -> str:
        return 'APL'

    def generate_event(self, name: str) -> None:
        with open(name, 'w+') as file:
            yaml.dump(self.model_dump(), file)

class ColonyMoon(Mission):
    size: int

    def __str__(self) -> str:
        return f'{super().__str__()}CLMN'

class GalaxyTwo(Mission):
    galaxy_name: str

    def __str__(self) -> str:
        return f'{super().__str__()}GALXONE'

class OrbitOne(Mission):
    model_config = ConfigDict(use_enum_values = True)
    satellite_name: str
    service_type: ServiceType

    def __str__(self) -> str:
        return f'{super().__str__()}ORBONE'

class Unkn(Mission):

    @property
    def mission(self) -> str:
        return super().mission.upper()

    def __str__(self) -> str:
        return f'{super().__str__()}UNKN'

    @property
    def hash(self):
        '''
        Overrides hash property in order to disable hash generation

        Parameters:
        -----------

        Returns:
        --------
            None
        '''

        return None

    @computed_field
    @property
    def process_id(self) -> str:
        return str(uuid.uuid4())

class VacMars(Mission):

    number_of_passengers: int
    ticket_price: float

    @computed_field
    @property
    def total_sales(self) -> float:
        return self.number_of_passengers * self.ticket_price

    def __str__(self) -> str:
        return f'{super().__str__()}TMRS'
