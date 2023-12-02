from mission import Mission

class GalaxyTwo(Mission):
    def __init__(self, galaxy_name: str, distance_ly: int) -> None:
        self.__galaxy_name = galaxy_name
        self.__distance_ly = distance_ly
