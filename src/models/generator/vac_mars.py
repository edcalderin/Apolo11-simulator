class VacMars:
    def __init__(self, number_of_passengers: int, ticket_price: float) -> None:
        self.number_of_passengers = number_of_passengers
        self.ticket_price = ticket_price
    
    def calculate_total(self)->float:
        return self.number_of_passengers*self.ticket_price
        