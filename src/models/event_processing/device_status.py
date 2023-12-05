from enum import Enum

class DeviceType(Enum):
    EXCELLENT = 'Excellent'
    GOOD = 'Good'
    WARNING = 'Warning'
    FAULTY = 'Faulty'
    KILLED = 'Killed'
    UNKNOWN = 'Unknown'
