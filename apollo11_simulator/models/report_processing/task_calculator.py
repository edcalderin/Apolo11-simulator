import pandas as pd
from typing import Tuple

class TaskCalculator:
    def __init__(self, events: pd.DataFrame) -> None:
        self.__events = events

    def task_event_analysis(self) -> Tuple[str, pd.DataFrame]:
        result = self.__events.groupby(['mission', 'device_status'])['device_type'].count().rename('Count').to_frame()
        return "*** CANTIDAD DE ESTADOS POR MISION ***", result

    def task_disconnection_management(self) -> Tuple[str, pd.DataFrame]:
        unkn_devices = self.__events[self.__events.device_status == 'UNKNOWN']
        result = unkn_devices.groupby(['mission', 'device_type'])['device_status'].count().rename('Count').to_frame()
        return "*** DISPOSITIVOS DESCONECTADOS POR MISION ***", result

    def task_mission_consolidation(self) -> Tuple[str, pd.DataFrame]:
        killed_devices = self.__events[self.__events.device_status == 'KILLED']
        result = killed_devices['device_type'].value_counts().to_frame()
        return "*** CANTIDAD DE DISPOSITIVOS INOPERABLES ***", result

    def task_devices_by_mission(self) -> Tuple[str, pd.DataFrame]:
        result = self.__events.groupby(['mission', 'device_type'])['device_type'].count().rename('Count').to_frame()
        return "*** CANTIDAD DE DISPOSITIVOS POR MISION ***", result

    def task_per_devices_by_mission(self) -> Tuple[str, pd.DataFrame]:
        devices_by_mission_ = self.task_devices_by_mission()[1]
        percentages = (devices_by_mission_/ devices_by_mission_.groupby(level=0).sum()) * 100
        result = percentages.map(lambda x: f'{x:.2f} %')
        return "*** PORCENTAJE DE DISPOSITIVOS POR MISION ***", result

    def task_mission_by_device_status(self) -> Tuple[str, pd.DataFrame]:
        mission_by_device_status_ = self.__events.groupby(['mission', 'device_status'])['device_status']\
            .count().rename('count')
        result = (mission_by_device_status_ / mission_by_device_status_.groupby(level=0).sum()) * 100
        return "*** PORCENTAJE DE ESTADO DE DISPOSITIVOS POR MISION ***", result

    def task_status_by_device_type_by_mission(self) -> Tuple[str, pd.DataFrame]:
        result = self.__events.groupby(
            ['mission', 'device_type', 'device_status'])['device_status'].count().rename('count')
        return "*** CANTIDAD DE ESTADOS POR DISPOSITIVO POR MISION ***", result

    def task_per_status_by_device_type_by_mission(self) -> Tuple[str, pd.DataFrame]:
        mission_by_devices_data = self.task_status_by_device_type_by_mission()[1]
        percentages = (mission_by_devices_data / mission_by_devices_data.groupby(level=0).sum()) * 100
        result = percentages.map(lambda x: f'{x:.2f} %')
        return "*** PORCENTAJE DE ESTADOS POR DISPOSITIVO POR MISION  ***", result
