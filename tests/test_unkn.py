# import pytest
# import uuid  # Importa el módulo uuid
# from datetime import datetime
# from apollo11_simulator.models.event_processing.mission import Unkn
# from apollo11_simulator.models.event_processing.device import Device
# from apollo11_simulator.models.event_processing.device_status import DeviceStatus

# def test_generate_event_for_unkn():
        
#     # Definir una lista de dispositivos con todos los campos requeridos
#     device = Device(device_type="TypeA", device_status=DeviceStatus.EXCELLENT, device_age=2)
    
    
#     # Crear una instancia de Unkn con los parámetros definidos
#     date = datetime(2023, 1, 1)    
#     unkn_instance = Unkn(date=date, budget="unknown", device=device) 
    
#     # Generar el evento para la instancia Unkn
#     unkn_instance.generate_event()
    
    
# # Ejecutar las pruebas con pytest
# if __name__ == "__main__":
#     pytest.main([__file__])