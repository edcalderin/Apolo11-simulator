import pandas as pd
from typing import Tuple

class TaskCalculator:
    def __init__(self, events: pd.DataFrame) -> None:
        self.__events = events

    def task_event_analysis(self) -> Tuple[str, pd.DataFrame]:
        result = self.__events.groupby(['mission', 'device_status'])['device_type'].count().rename('Count').to_frame()
        return "*** CANTIDAD DE ESTADOS POR MISION ***", result

    def task_disconnection_management(self) -> Tuple[str, pd.DataFrame]:
        unkn_devices = self.__events[self.__events.device_status == 'unknown']
        result = unkn_devices.groupby(['mission', 'device_type'])['device_status'].count().rename('Count').to_frame()
        return "*** DISPOSITIVOS DESCONECTADOS POR MISION ***", result

    def task_mission_consolidation(self) -> Tuple[str, pd.DataFrame]:
        killed_devices = self.__events[self.__events.device_status == 'killed']
        result = killed_devices['device_type'].value_counts().to_frame()
        return "*** CANTIDAD DE DISPOSITIVOS INOPERABLES ***", result

    def task_devices_by_mission(self) -> Tuple[str, pd.DataFrame]:
        devices_by_mission = self.__events.groupby(['mission', 'device_type'])['device_type'].count().rename('Count')
        percentages = (devices_by_mission / devices_by_mission.groupby(level=0).sum()) * 100
        percentages = percentages.map(lambda x: f'{x:.2f} %').rename("percentage").to_frame()
        devices_by_mission = devices_by_mission.to_frame()
        devices_by_mission["percentage"] = percentages["percentage"]
        return "*** CANTIDAD DE DISPOSITIVOS POR MISION ***", devices_by_mission

    def task_mission_by_device_status(self) -> Tuple[str, pd.DataFrame]:
        mission_by_device_status_ = self.__events.groupby(['mission', 'device_status'])['device_status']\
            .count().rename('count')
        result = (mission_by_device_status_ / mission_by_device_status_.groupby(level=0).sum()) * 100
        return "*** PORCENTAJE DE ESTADO DE DISPOSITIVOS POR MISION ***", result

    def task_status_by_device_type_by_mission(self) -> Tuple[str, pd.DataFrame]:
        mission_by_devices_data = self.__events.groupby(
            ['mission', 'device_type', 'device_status'])['device_status'].count().rename('count')
        percentages = (mission_by_devices_data / mission_by_devices_data.groupby(level=0).sum()) * 100
        percentages = percentages.map(lambda x: f'{x:.2f} %').rename("percentage").to_frame()
        mission_by_devices_data = mission_by_devices_data.to_frame()
        mission_by_devices_data["percentage"] = percentages["percentage"]
        return "*** CANTIDAD DE ESTADOS POR DISPOSITIVO POR MISION ***", mission_by_devices_data


