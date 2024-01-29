import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict

import pandas as pd
from yaml import YAMLError

from apollo11_simulator.common import Logger, Utils
from apollo11_simulator.exceptions import UnfoundEventsError
from apollo11_simulator.models.report_processing.report_title import REPORT_TITLE
from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator

logger = Logger.get_logger("report_builder")

class ReportBuilder:
    """Class to read events and process files."""

    def __init__(self,
                 events: pd.DataFrame,
                 devices_path: Path,
                 backup_path: Path) -> None:
        """Initialize the class object.

        Args:
            events (pd.DataFrame): Dataframe with events
            devices_path (str): Path containing directory of devices
            backup_path (Path): Destination path for processed events
        """
        self.__events = events
        self.__devices_path = devices_path
        self.__backup_path = backup_path

    @classmethod
    def read_events(cls, devices_path: str, backup_path: str) -> None:
        """
        To read files from path and merge content in str.

        Parameters:
        --------
        - devices_path: Path containing the event files
        - backup_path: Path to save the report

        Returns:
        --------
        None
        """
        try:
            devices_path = Path(devices_path)

            logger.info(f'Processing events from {devices_path.absolute()}')

            events_df = cls._events_to_dataframe(cls, devices_path)

            # Create backup directoy if it does not exist
            backup_path = Path(backup_path)
            backup_path.mkdir(exist_ok = True)

            return cls(events = events_df,
                       devices_path = devices_path,
                       backup_path = backup_path)

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

    def _events_to_dataframe(self, devices_path: Path) -> pd.DataFrame:
        events = pd.DataFrame.from_records(
            filter(lambda y: y is not None,
                map(self._read_file_map,
                    devices_path.glob('**/*.log'))))

        if not len(events):
            raise UnfoundEventsError(
                f'Directory {devices_path.absolute()} either doesn\'t exist or '\
                'contains invalid event files')

        events = pd.concat([events, pd.json_normalize(events["device"])], axis=1)
        events.drop("device", inplace=True, axis=1)
        return events

    def __call__(self):
        """Process the events and move the processed files to the destination path."""
        task_calculator = TaskCalculator(self.__events)
        line_jump = ['\n']*2
        report_name = Path(
            f'APLSTATS-REPORTE-{Utils.transform_date(datetime.now())}.log')

        with open(report_name, "w+") as file:
            file.write(REPORT_TITLE)

            for attr in dir(task_calculator):
                # Filtering the task_calculator attributes by "task_" pattern.
                # These attributes correspond to methods that return a particular report
                if attr.startswith('task_'):
                    report_title, report_df = getattr(task_calculator, attr)()
                    file.write(f'{report_title}\n')
                    file.write(report_df.to_string())
                    file.writelines(line_jump)
                    file.write('='*85)
                    file.writelines(line_jump)

        logger.info(f'Report generated successfully in {report_name.absolute()}')

        logger.info(f'Moving subdirectories to {self.__backup_path.absolute()}')

        iter_count: int = 1

        for path in self.__devices_path.iterdir():
            shutil.move(path, self.__backup_path)
            iter_count += 1
        else:
            logger.info(f'{iter_count} events subdiretories were found and moved!')
