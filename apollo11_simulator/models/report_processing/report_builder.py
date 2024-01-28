import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict

import pandas as pd
from yaml import YAMLError

from apollo11_simulator.common import Utils, Logger
from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator

logger = Logger.get_logger("report_builder")

class ReportBuilder:

    def __init__(self, events: pd.DataFrame,
                 origin_path: str,
                 target_path: str) -> None:
        self.__events = events
        self.__origin_path = origin_path
        self.__target_path = target_path

    @classmethod
    def read_events(cls, origin_path: str, target_path: str) -> None:
        '''
        To read files from path and merge content in str

        Parameters:
        --------
        - origin_path: Path containing the event files
        - target_path: Path to save the report

        Returns:
        --------
        None
        '''

        events_df = cls.events_to_dataframe(cls, origin_path)

        return cls(events_df, origin_path, target_path)

    @staticmethod
    def _read_file_map(file_name) -> Dict:
        try:
            event = Utils.read_yaml(file_name)
        except YAMLError:
            logger.warning(f'File {file_name} was ignored')
            event = None
        except Exception as exc:
            logger.error(f'Report builder has stopped {str(exc)}')
            exit(-1)

        return event

    def events_to_dataframe(self, origin_path: str) -> pd.DataFrame:
        events = pd.DataFrame.from_records(
            filter(lambda y: y is not None,
                   map(self._read_file_map,
                       Path(origin_path).glob('*.log'))))
        if not len(events):
            print('No events')
            raise 
        events = pd.concat([events, pd.json_normalize(events["device"])], axis=1)
        events.drop("device", inplace=True, axis=1)
        return events

    def __call__(self):
        logger.info(f'Processing events from {Path(self.__origin_path).absolute()}')
        task_calculator = TaskCalculator(self.__events)
        line_jump = ['\n']*2
        report_name: str = f"APLSTATS-REPORTE-{Utils.transform_date(datetime.now())}.log" # noqa

        with open(report_name, "w+") as file:

            for attr in dir(task_calculator):
                # Filtering the task_calculator attributes by "task_" pattern.
                # These attributes correspond to methods that return a particular report
                if attr.startswith('task_'):
                    report_title, report_df = getattr(task_calculator, attr)()
                    file.write(f'{report_title}\n')
                    file.write(f'{report_df.to_string()}\n')
                    file.writelines(line_jump)
                    file.write('='*100)
                    file.writelines(line_jump)

        logger.info(f'Moving files to {Path(self.__target_path).absolute()}')
        shutil.move(self.__origin_path, self.__target_path)
