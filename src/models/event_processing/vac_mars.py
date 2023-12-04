from mission import Mission
from pydantic import BaseModel

class VacMars(Mission, BaseModel):

    number_of_passengers: int
    ticket_price: float

    @property
    def total_sales(self) -> float:
        return self.number_of_passengers * self.ticket_price
