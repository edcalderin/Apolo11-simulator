from mission import Mission
from pydantic import BaseModel

class Unkn(Mission, BaseModel):
    uuid: str