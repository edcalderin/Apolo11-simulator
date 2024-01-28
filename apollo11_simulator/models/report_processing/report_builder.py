import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict

import pandas as pd
from yaml import YAMLError

from apollo11_simulator.common import Logger, Utils
from apollo11_simulator.exceptions import UnfoundEventsError
from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator

logger = Logger.get_logger("report_builder")

class ReportBuilder:

    def __init__(self, events: pd.DataFrame,
                 origin_path: str,
                 target_path: str) -> None:
        self.__events = events
        self.__origin_path = Path(origin_path)
        self.__target_path = Path(target_path)

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
        try:
            events_df = cls.events_to_dataframe(cls, Path(origin_path))

            return cls(events_df, origin_path, target_path)
        except UnfoundEventsError as unfound_error:
            logger.error(str(unfound_error))
            exit(-1)

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

    def events_to_dataframe(self, origin_path: Path) -> pd.DataFrame:
        events = pd.DataFrame.from_records(
            filter(lambda y: y is not None,
                map(self._read_file_map,
                    origin_path.glob('*.log'))))

        if not len(events):
            raise UnfoundEventsError(
                f'Directory {origin_path.absolute()} either doesn\'t exist or '\
                'contains invalid event files')

        events = pd.concat([events, pd.json_normalize(events["device"])], axis=1)
        events.drop("device", inplace=True, axis=1)
        return events

    def __call__(self):
        logger.info(f'Processing events from {self.__origin_path.absolute()}')
        task_calculator = TaskCalculator(self.__events)
        line_jump = ['\n']*2
        report_name = Path(f'APLSTATS-REPORTE-{Utils.transform_date(datetime.now())}.log') # noqa

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

        logger.info(f'Report generated successfully in {report_name.absolute()}')

        logger.info(f'Moving files to {self.__target_path.absolute()}')
        shutil.move(self.__origin_path, self.__target_path)
