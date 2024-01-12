from src.models.event_processing.mission import Mission
import uuid
from pydantic import computed_field



class Unkn(Mission):
    
    
    @computed_field
    @property
    def process_id(self) -> str:
        return str(uuid.uuid4())
    
    def generate_event(self) -> None:
        name: str = f'APLUNKN-0001.log'
        
        super().generate_event(name)
        