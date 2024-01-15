from datetime import datetime


class Utils:

    @staticmethod
    def to_ddmmyyHHMISS(date: datetime) -> str:
        custom_format = "%d%m%y%H%M%S"
        return date.strftime(custom_format)
