from mission import Mission

class GalaxyTwo(Mission):
    galaxy_name: str
    distance_ly: int

    def generate_event(self) -> None:
        name: str = f'APLGALXONE-0001.log'
        super().generate_event(name)