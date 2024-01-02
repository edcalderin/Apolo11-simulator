import pytest
from datetime import datetime
from src.models.event_processing.unkn import Unkn
from src.models.event_processing.device import Device
from src.models.event_processing.device_status import DeviceStatus

def test_generate_event_for_unkn():
    # Definir una lista de dispositivos con todos los campos requeridos
    devices = [
        Device(id=1, device_type="TypeA", device_status=DeviceStatus.EXCELLENT, device_age=2),
        Device(id=2, device_type="TypeB", device_status=DeviceStatus.GOOD, device_age=3)
    ]
    
    # Crear una instancia de Unkn con los parámetros definidos
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 10)
    budget = 1000.0
    unkn_instance = Unkn(start_date=start_date, end_date=end_date, budget=budget, devices=devices)
    
    # Generar el evento para la instancia Unkn
    unkn_instance.generate_event()
    
    # Aquí podrías agregar aserciones adicionales si deseas verificar algo específico después de generar el evento.

# Ejecutar las pruebas con pytest
if __name__ == "__main__":
    pytest.main([__file__])