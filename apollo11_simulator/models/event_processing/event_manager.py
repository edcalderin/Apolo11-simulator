from typing import Any, List, Tuple
from pydantic import BaseModel, Field, field_validator
from apollo11_simulator.models.event_processing.mission import ColonyMoon, GalaxyTwo, OrbitOne, Unkn, VacMars
from apollo11_simulator.models.event_processing.device import Device
from apollo11_simulator.models.event_processing.device_status import DeviceStatus
from apollo11_simulator.models.event_processing.service_type import ServiceType
from datetime import datetime
import random
from pathlib import Path
from time import sleep

class EventManager(BaseModel):
    '''
    Generate event files in yaml format by calling the instance of the class:

    Example:

    event_manager = EventManager(...)\n
    event_manager()

    Attributes:
    ----------
    - target_path: Directory name, it will be created if it does not exist
    - frequency_seconds: Frequency in seconds at which event files will be generated
    - range_of_files: A tuple with 2 values indicating the minimum and maximun number
    of events to generate in each iteration
    '''

    target_path: str = Field(min_length = 1)
    frequency_seconds: int = Field(gt = 0)
    range_of_files: Tuple[int, int]

    @field_validator('range_of_files')
    def validate_range_of_files(cls, values: Tuple[int, int]) -> Tuple[int, int]:
        '''
        Validate the range_of_file with the following rules:
        - Both Values must be positive.
        - Both values must be different from zero.
        - The second value must be greater than the first one.

        Returns:
        --------
        Value of the tuple
        '''

        v1, v2 = values

        if v1 < 0 or v2 < 0:
            raise ValueError('All the values must be positive')

        if v1 == v2 == 0:
            raise ValueError('Both values must be different from zero')

        if v1 > v2:
            raise ValueError('The second value must be greater than the first one')

        return values

    def __random_device(self, mission_class) -> Device:
        '''
        Return a random device of type Device class

        Parameters:
        -----------
        - mission_class: Class which inherits from Mission class, if it is Unkn class
        then it will return a Device object with hardcoded values equal to "unknown"

        Returns:
        --------
        Object of Device type
        '''

        if mission_class is Unkn:
            return Device(
                device_type = 'unknown',
                device_status = DeviceStatus.UNKNOWN,
                device_age = 'unknown',
                device_description = 'unknown'
            )
        else:
            return Device(
                device_status = random.choice([
                    DeviceStatus.EXCELLENT,
                    DeviceStatus.FAULTY,
                    DeviceStatus.GOOD,
                    DeviceStatus.KILLED,
                    DeviceStatus.WARNING,
                    DeviceStatus.UNKNOWN
                ]),
                device_type = 'd',
                device_description = 'any description',
                device_age = random.randint(2, 20)
            )

    def __generate_files(self, epoch: int) -> None:
        '''
        Generate events in yaml format

        Parameters:
        -----------
        - epoch: Current iteration

        Returns:
        --------
        None
        '''

        print('Generating files...')

        min_files, max_files = self.range_of_files

        number_of_files: int = random.randint(min_files, max_files)

        mission_classes: List = random.choices([ColonyMoon, OrbitOne, GalaxyTwo, VacMars, Unkn], k = number_of_files)

        # Create "devices" directory if it does not exist
        device_path = Path(self.target_path)
        device_path.mkdir(exist_ok = True)

        for i, mission_class in enumerate(mission_classes, 1):

            # Params for each mission class whose keys correspond to the class
            mission_params = {
                ColonyMoon: {
                    'date': datetime.now(),
                    'budget': 2,
                    'size': 5
                },
                OrbitOne: {
                    'date' : datetime.now(),
                    'budget' : 2,
                    'satellite_name' : 'OpenAI',
                    'service_type' : ServiceType.UPDATE
                },
                GalaxyTwo: {
                    'date': datetime.now(),
                    'budget': 2,
                    'distance_ly': 15,
                    'galaxy_name': 'Orion'
                },
                VacMars: {
                    'date': datetime.now(),
                    'budget': 2,
                    'number_of_passengers': 3,
                    'ticket_price': 15
                },
                Unkn: {
                    'date': datetime.now(),
                    'budget': 'unknown'
                }
            }

            # Create an instance based on one of the dictionary keys.
            mission_instance = mission_class(**mission_params[mission_class], device = self.__random_device(mission_class))

            name: Path = device_path.joinpath(f'{str(mission_instance)}-{epoch}{i}.log')

            mission_instance.generate_event(name)

    def __call__(self) -> Any:
        try:
            epoch: int = 0

            while True:
                self.__generate_files(epoch)
                sleep(self.frequency_seconds)
                epoch += 1

        except KeyboardInterrupt:
            print('The process was interrupted!')
        except Exception as e:
            print(str(e))