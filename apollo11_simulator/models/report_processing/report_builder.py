from pathlib import Path
from datetime import datetime
import shutil
import pandas as pd

from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator
from apollo11_simulator.utils import Utils
from yaml import YAMLError

class ReportBuilder:

    def __init__(self, events: pd.DataFrame, origin_path: str, target_path: str) -> None:
        self.__events = events
        self.__origin_path = origin_path
        self.__target_path = target_path

    @classmethod
    def read_events(cls, origin_path: str, target_path: str):
        '''
        To read files from path and merge content in str

        Parameters:
        - origin_path: path where the files to read are located
        Returns:
            str
        '''

        events_df = cls.events_to_dataframe(cls, origin_path)

        return cls(events_df, origin_path, target_path)

    @staticmethod
    def read_file_map(filename) -> dict:
        try:
            event = Utils.read_yaml(filename)
        except YAMLError:
            print(f'File {filename} was ignored')
            event = None
        except Exception as exc:
            print('Report builder has stopped', str(exc))
            exit(-1)

        return event

    def events_to_dataframe(self, origin_path: str) -> pd.DataFrame:
        events = pd.DataFrame.from_records(filter(lambda y: y is not None, map(self.read_file_map, Path(origin_path).glob('*.log'))))

        events = pd.concat([events, pd.json_normalize(events["device"])], axis=1)
        events.drop("device", inplace=True, axis=1)
        return events

    def __call__(self):
        task_calculator = TaskCalculator(self.__events)
        line_jump = ['\n']*2
        report_name: str = f"APLSTATS-REPORTE-{Utils.transform_date(datetime.now())}.log"
        with open(report_name, "w+") as file:
            for attr in dir(task_calculator):
            # Getting all the attributes of task_calculator object to filter by "task_" pattern.
            # These attributes correspond to methods that return a particular report
                if attr.startswith('task_'):
                    report_title, report_df = getattr(task_calculator, attr)()
                    file.write(f'{report_title}\n')
                    file.write(f'{report_df.to_string()}\n')
                    file.writelines(line_jump)
                    file.write('='*100)
                    file.writelines(line_jump)

        print('Moving files...')
        shutil.move(self.__origin_path, self.__target_path)
