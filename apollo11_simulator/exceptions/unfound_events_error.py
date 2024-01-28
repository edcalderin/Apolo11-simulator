class UnfoundEventsError(Exception):

    def __init__(self, message: str) -> None:
        self.mensaje: str = message
