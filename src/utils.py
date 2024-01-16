from datetime import datetime


class Utils:

    @staticmethod
    def to_ddmmyyHHMISS(date: datetime) -> str:
        '''
        To transform date in format ddmmyyHHMMSS

        Parameters:
        - date: date in datetime format
        Returns:
            str
        '''
        custom_format = '%d%m%y%H%M%S'
        return date.strftime(custom_format)
