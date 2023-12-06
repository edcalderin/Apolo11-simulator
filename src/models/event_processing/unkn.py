from mission import Mission

class Unkn(Mission):
    uuid: str
    
    def generate_event(self) -> None:
        name: str = f'APLUNKN-0001.log'
        super().generate_event(name)