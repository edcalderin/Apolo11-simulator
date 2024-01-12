from typing import Any, List, Tuple
from pydantic import BaseModel
from src.models.event_processing.colony_moon import ColonyMoon
from src.models.event_processing.device import Device
from src.models.event_processing.device_status import DeviceStatus
from src.models.event_processing.galaxy_two import GalaxyTwo
from src.models.event_processing.orbit_one import OrbitOne
from src.models.event_processing.service_type import ServiceType
from src.models.event_processing.vac_mars import VacMars
from src.models.event_processing.unkn import Unkn
from datetime import datetime
import random
from pathlib import Path

class EventManager(BaseModel):
    frequency_seconds: int
    number_of_files: Tuple[int, int]

    def __generate_files(self):
        min_files, max_files = self.number_of_files
        n_files: int = random.randint(min_files, max_files)
        choices: List = random.choices([ColonyMoon, GalaxyTwo, OrbitOne, VacMars, Unkn], k = n_files)
        
        device_path = Path('devices')
        device_path.mkdir(exist_ok=True) 
             
        for i, choice in enumerate(choices):
            if choice is ColonyMoon:
                name: Path = device_path.joinpath(f'APLCLMN-{i}.log')
                colony_moon = ColonyMoon(
                    date = datetime.now(), 
                    budget = 2,
                    size = 5,
                    device = Device(device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)
                )
                colony_moon.generate_event(name)
                
            elif choice is OrbitOne:
                name: Path = device_path.joinpath(f'APLORBONE-{i}.log')
                orbit_one = OrbitOne(
                    date = datetime.now(), 
                    budget = 2,
                    satellite_name = 'OpenAI',
                    service_type = ServiceType.UPDATE,
                    device = Device(device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)
                )
                orbit_one.generate_event(name)
                
            elif choice is GalaxyTwo:
                name: Path = device_path.joinpath(f'APLGALXONE-{i}.log')
                galaxy_two = GalaxyTwo(
                    date = datetime.now(), 
                    budget = 2,
                    distance_ly = 15,
                    galaxy_name='Orion',
                    device = Device(device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)
                )
                galaxy_two.generate_event(name)
                
            elif choice is VacMars:
                name: Path = device_path.joinpath(f'APLTMRS-{i}.log')
                vac_mars = VacMars(
                    date = datetime.now(), 
                    budget = 2,
                    number_of_passengers= 3,
                    ticket_price = 15,
                    device = Device(device_status=DeviceStatus.EXCELLENT, device_type='d', device_age=2)
                )
                vac_mars.generate_event(name)

            elif choice is Unkn:
                name: Path = device_path.joinpath(f'APLUNKN-{i}.log')
                unkn = Unkn(date=datetime.now(),
                            budget='unknown', 
                            device=Device(device_type='unknown', device_status=DeviceStatus.UNKNOWN, device_age='unknown'))
                unkn.generate_event(name)
                
    def __call__(self) -> Any:
        # aqui va schedule
        self.__generate_files()