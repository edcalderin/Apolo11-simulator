from enum import Enum


class DeviceStatus(Enum):
    EXCELLENT = 'excellent'
    GOOD = 'good'
    WARNING = 'warning'
    FAULTY = 'faulty'
    KILLED = 'killed'
    UNKNOWN = 'unknown'
