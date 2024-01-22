from datetime import datetime
from pathlib import Path
import yaml
from typing import Dict
import json
from apollo11_simulator.decorators import CatchFileExceptions

class Utils:
    '''
    Class with important utilities ready to be re-used,
    these are static methods that can be invoked without instantiating the class.
    '''

    @staticmethod
    def to_ddmmyyHHMISS(date: datetime) -> str:
        '''
        To transform date in format ddmmyyHHMMSS

        Parameters:
        -----------
        - date: date in datetime format

        Returns:
        --------
            str
        '''
        custom_format = '%d%m%y%H%M%S'
        return date.strftime(custom_format)

    @staticmethod
    @CatchFileExceptions
    def read_yaml(path: Path) -> Dict:
        '''
        Read a yaml file given a path

        Parameters:
        -----------
        - path: Path of the file as Path object

        Returns:
        --------
        Dictionary containing items from the file.

        Exceptions:
        -----------
        - YAMLError: Invalid yaml file
        - Exception: Error by reading file
        '''
        with open(path) as file:
            return yaml.safe_load(file)

    @staticmethod
    @CatchFileExceptions
    def read_json(path: Path) -> Dict:
        '''
        Read a json file given a path

        Parameters:
        -----------
        - path: Path of the file as Path object

        Returns:
        --------
        Dictionary containing items from the file.

        Exceptions:
        -----------
        - JSONDecodeError: Invalid json file
        - Exception: Error by reading file
        '''
        with open(path) as file:
            return json.load(file)
