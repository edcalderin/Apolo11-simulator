"""UnfoundEventsError exception module."""

class UnfoundEventsError(Exception):
    """Custom exception.

    Must be raised when the devices directory either does not exist or contains invalid
    event files.
    """

    def __init__(self, message: str) -> None:
        """Initialize the exception.

        Args:
            message (str): Message to show in the exception
        """
        self.mensaje: str = message
