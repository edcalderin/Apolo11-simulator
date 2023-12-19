from src.models.event_processing.mission import Mission
from typing import Tuple

class ColonyMoon(Mission):
    size: int
    location: Tuple[float, float]
    
    def generate_event(self) -> None:
        name: str = f'APLCLNM-0001.log'
        super().generate_event(name)