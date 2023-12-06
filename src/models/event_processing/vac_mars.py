from mission import Mission
import yaml

class VacMars(Mission):

    number_of_passengers: int
    ticket_price: float

    @property
    def total_sales(self) -> float:
        return self.number_of_passengers * self.ticket_price

    def generate_event(self) -> None:
        name: str = f'APLTMRS-0001.log'
        super().generate_event(name)