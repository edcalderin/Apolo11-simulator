from enum import Enum


class ServiceType(Enum):
    """Enumerable that contains possible services type for OrbitOne mission."""

    UPDATE = 'Update'
    REPARATION = 'Reparation'
    REPLACEMENT = 'Replacement'
