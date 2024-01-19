import os
from pathlib import Path
from apollo11_simulator.models.report_processing.task_calculator import TaskCalculator

class ReportBuilder:
    __task_calculator: TaskCalculator

    def __init__(self, events) -> None:
        self.__events: dict

    @classmethod
    def from_path(cls, origin_path: str) -> str:
        '''
        To read files from path and merge content in str

        Parameters:
        - origin_path: path where the files to read are located
        Returns:
            str
        '''

        list_files = os.listdir(origin_path)
        content_merge = ''
        for file in list_files:
            with open(origin_path + '/' + file, "r") as content_file:
                for line in content_file:
                    if line != '':
                        content_merge += line.strip() + "\n"
            cls.move_files(origin_path, 'backup', file) # TODO: get target path from config file
        return content_merge

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

    def show_report():
        pass