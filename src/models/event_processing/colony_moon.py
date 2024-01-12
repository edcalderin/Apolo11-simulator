from src.models.event_processing.mission import Mission

class ColonyMoon(Mission):
    size: int
    
    def __str__(self) -> str:
        return f'{super().__str__()}CLMN'