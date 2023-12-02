from mission import Mission

class ColonyMoon(Mission):
    def __init__(self, size: int, latitude: float, longitude: float) -> None:
        self.__size = size
        self.__latitude = latitude
        self.__longitude = longitude
