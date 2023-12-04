from mission import Mission
from pydantic import BaseModel
from typing import Tuple

class ColonyMoon(Mission, BaseModel):
    size: int
    location: Tuple[float, float]