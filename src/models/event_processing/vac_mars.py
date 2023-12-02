from mission import Mission

class VacMars(Mission):
    def __init__(self, number_of_passengers: int, ticket_price: float) -> None:
        self.__number_of_passengers = number_of_passengers
        self.__ticket_price = ticket_price

    @property
    def total_sales(self)->float:
        return self.__number_of_passengers * self.__ticket_price
