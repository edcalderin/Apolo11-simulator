class Mission:
    def __init__(self, start_date: str, end_date: str, budget: float, devices) -> None:
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.devices = devices
    
    def calculate_duration(self)->str:
        pass
    
    def generate_event(self)->None:
        pass