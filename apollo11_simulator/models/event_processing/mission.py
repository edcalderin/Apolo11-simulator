"""Mission module that contains class definitions for the event processing."""

import hashlib
import uuid
from datetime import datetime

import yaml
from pydantic import BaseModel, ConfigDict, computed_field

from apollo11_simulator.common import Utils
from apollo11_simulator.models.event_processing.device import Device
from apollo11_simulator.models.event_processing.service_type import ServiceType


class Mission(BaseModel):
    """Class that represents a general mission.

    Args:
        date (datetime): Date
        budget (float | str): Budget for this mission. It allows a float number or
        string, particularly "unknown" value
        device (Device): Object of Device type

    """

    date: datetime
    budget: float | str
    device: Device

    @computed_field
    @property
    def mission(self) -> str:
        """Returns the name of the class.

        Returns:
        --------
            str
        """
        return self.__class__.__name__

    @computed_field
    @property
    def hash(self) -> str:
        """Overrides hash property in order to disable hash generation.

        Returns:
        --------
            str
        """
        hash = hashlib.sha256()
        hash.update(Utils.transform_date(self.date).encode())
        hash.update(self.mission.encode())
        hash.update(self.device.device_type.encode())
        hash.update(self.device.device_status.encode())
        return hash.hexdigest()

    def __str__(self) -> str:
        """Define the prefix name for the subclasses.

        The result will be concatenated with their individual names.

        Example:
        >> APL{str(sublcass)}

        Returns:
            str: Prefix name for the mission names
        """
        return 'APL'

    def generate_event(self, name: str) -> None:
        """Create a yaml file with a name received as parameter.

        Args:
            name (str): Name of the log file

        Returns:
            None
        """
        with open(name, 'w+') as file:
            yaml.dump(self.model_dump(), file)


class ColonyMoon(Mission):
    """Class that inherits from Mission.

    Mission to establish a colony on the moon.

    Args:
        Mission (_type_): _description_

    Returns:
        size (int): Number of astronauts in the colony
    """

    size: int

    def __str__(self) -> str:
        """Create the mission name.

        Construct the mission name by utilizing the __str__ magic method from the
        Mission class along with the current value. This composed name will serve as
        the filename.

        Returns:
            str: String that represents the name of the current mission
        """
        return f'{super().__str__()}CLMN'


class GalaxyTwo(Mission):
    """Subclass that inherits from Mission which represents the GalaxyTwo mission.

    Args:
        galaxy_name (str): Name of the galaxy

    """

    galaxy_name: str

    def __str__(self) -> str:
        """Create the mission name.

        Construct the mission name by utilizing the __str__ magic method from the
        Mission class along with the current value. This composed name will serve as
        the filename.

        Returns:
            str: String that represents the name of the current mission
        """
        return f'{super().__str__()}GALXONE'


class OrbitOne(Mission):
    """Subclass that inherits from Mission.

    The goal of this mission is to modernize
    the entire fleet of satellites with the aim of enhancing their performance and
    improving coverage and communications.

    Args:
        satellite_name (str): Name of satallite
        service_type (ServiceType): Type of service

    """

    model_config = ConfigDict(use_enum_values=True)
    satellite_name: str
    service_type: ServiceType

    def __str__(self) -> str:
        """Create the mission name.

        Construct the mission name by utilizing the __str__ magic method from the
        Mission class along with the current value. This composed name will serve as
        the filename.

        Returns:
            str: String that represents the name of the current mission
        """
        return f'{super().__str__()}ORBONE'


class Unkn(Mission):
    """Subclass that inherits from Mission. This mission is undefined or unknown."""

    @property
    def mission(self) -> str:
        """Convert the name of the class to upper case.

        Returns:
            str: Name of the class in upper case
        """
        return super().mission.upper()

    def __str__(self) -> str:
        """Create the mission name.

        Construct the mission name by utilizing the __str__ magic method from the
        Mission class along with the current value. This composed name will serve as
        the filename.

        Returns:
            str: String that represents the name of the current mission
        """
        return f'{super().__str__()}UNKN'

    @property
    def hash(self):
        """Overrides hash property in order to disable hash generation.

        Returns:
        --------
            None
        """
        return None

    @computed_field
    @property
    def process_id(self) -> str:
        """Generates an UUID value as process id."""
        return str(uuid.uuid4())


class VacMars(Mission):
    """Sublass that inherits from Mission.

    Mission to take people on tourist trips to Mars

    Args:
        number_of_passengers (int): Number of tourists
        ticket_price (float): Ticket price per tourist
    """

    number_of_passengers: int
    ticket_price: float

    @computed_field
    @property
    def total_sales(self) -> float:
        """
        Returns the total sales as product of number of passenger and ticket price.

        Returns:
        --------
        float
        """
        return self.number_of_passengers * self.ticket_price

    def __str__(self) -> str:
        """Create the mission name.

        Construct the mission name by utilizing the __str__ magic method from the
        Mission class along with the current value. This composed name will serve as
        the filename.

        Returns:
            str: String that represents the name of the current mission
        """
        return f'{super().__str__()}TMRS'
