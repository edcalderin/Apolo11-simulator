from src.models.event_processing.mission import Mission

class Unkn(Mission):
    uuid: str

    @property
    def hash(self):
        '''
        Overrides hash property in order to disable hash generation
        
        Parameters:
        
        Returns:
            None
        '''
        return None
    
    def generate_event(self) -> None:
        name: str = f'APLUNKN-0001.log'
        super().generate_event(name)