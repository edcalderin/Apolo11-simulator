import os
from typing import List
from pathlib import Path


import pandas as pd

from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator
from apollo11_simulator.utils import Utils


class ReportBuilder:


    def __init__(self, events: pd.DataFrame) -> None:
        self.__events = events

    def yield_file(self, origin_path: str):
        for file in Path(origin_path).glob('*.log'):
            yield file

    @classmethod
    def read_events(cls, origin_path: str):
        '''
        To read files from path and merge content in str

        Parameters:
        - origin_path: path where the files to read are located
        Returns:
            str
        '''


        event_list: List = []
        for file in cls.yield_file(cls, origin_path):
            event = Utils.read_yaml(file)
            event_list.append(event)
            #cls.move_files(origin_path, 'backup', file) # TODO: get target path from config file

        events_df = cls.events_to_dataframe(cls, event_list)

        return cls(events_df)

    def events_to_dataframe(self, event_list: List) -> pd.DataFrame:
        events = pd.DataFrame.from_records(event_list)
        events = pd.concat([events, pd.json_normalize(events["device"])], axis=1)
        events.drop("device", inplace=True, axis=1)
        return events

    def move_files(self, origin_path: str, target_path: str, filename: str) -> None:
        '''
        To read files from path and merge content in str

        Parameters:
        - origin_path: path where the files to read are located
        - target_path: path where the file will be moved
        - filename: file name
        Returns:
            None
        '''
        Path(origin_path + '/' + filename).rename(target_path + '/' + filename)

    def show_report(self):
        task_calculator = TaskCalculator(self.__events)
        line_jump = ['\n']*2

        with open("report.txt", "w+") as file:
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
