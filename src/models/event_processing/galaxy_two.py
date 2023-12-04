from mission import Mission
from pydantic import BaseModel

class GalaxyTwo(Mission, BaseModel):
    galaxy_name: str
    distance_ly: int
