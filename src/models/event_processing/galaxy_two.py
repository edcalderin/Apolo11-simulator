from src.models.event_processing.mission import Mission

class GalaxyTwo(Mission):
    galaxy_name: str
    distance_ly: int

    def __str__(self) -> str:
        return f'{super().__str__()}GALXONE'
