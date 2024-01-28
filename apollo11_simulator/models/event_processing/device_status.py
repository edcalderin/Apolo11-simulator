"""DeviceStatus module."""
from enum import Enum


class DeviceStatus(Enum):
    """Enumerable with possible status for each device."""

    EXCELLENT = 'excellent'
    GOOD = 'good'
    WARNING = 'warning'
    FAULTY = 'faulty'
    KILLED = 'killed'
    UNKNOWN = 'unknown'
