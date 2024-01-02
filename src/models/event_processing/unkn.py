from typing import Optional  # Importa Optional desde el módulo typing
from src.models.event_processing.mission import Mission
import uuid
from datetime import datetime
import yaml

class Unkn(Mission):
    uuid: Optional[str] = None  # Usa Optional para indicar que el campo puede ser None
    _process_id: Optional[str] = None
    
    @property
    def process_id(self) -> str:
        """Getter para obtener el identificador UUID."""
        return self.uuid if self.uuid else "unknown"
    
    def generate_event(self) -> None:
        # Verificar si la misión UNKN está previamente definida en el registro
        if not self.uuid:
            self.uuid = str(uuid.uuid4())
            self._process_id = self.uuid  # Asignar el UUID a _process_id
        
        name: str = f'APLUNKN-0001.log'
        
        # Procesar los campos para generar el evento
        fields = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'mission': 'UNKN',
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'budget': str(self.budget),
            'devices': [device.model_dump() for device in self.devices],
            'duration': str(self.duration),
            'other_field': 'unknown',  # Marcar como "unknown" o cualquier otro procesamiento necesario
            # Agregar más campos y sus valores si es necesario
        }
        
        # Generar el evento con los campos procesados
        with open(name, 'w+') as file:
            yaml.dump(fields, file)