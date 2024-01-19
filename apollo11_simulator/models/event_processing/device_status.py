from enum import Enum

class DeviceStatus(Enum):
    EXCELLENT = 'Excellent'
    GOOD = 'Good'
    WARNING = 'Warning'
    FAULTY = 'Faulty'
    KILLED = 'Killed'
    UNKNOWN = 'Unknown'
