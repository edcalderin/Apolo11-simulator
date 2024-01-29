from json import JSONDecodeError
import time
from typing import Any, Callable, Dict
import psutil
import os
from yaml import YAMLError
from apollo11_simulator.common import Logger

current_pid = os.getpid()
logger = Logger.get_logger("decorators")

class CatchFileExceptions:
    """
    Decorator used to catch exceptions by reading yaml or json files.

    Exceptions:
    -----------
    - JSONDecodeError: Invalid json file
    - YAMLError: Invalid yaml file
    - Exception: Error by reading file
    """

    def __init__(self, function: Callable) -> None:
        """Initialize the class object.

        Args:
            function (Callable): Function to decorate
        """
        self._function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Contains the logic used for the decorator."""
        try:
            return self._function(*args, **kwds)

        except (YAMLError, JSONDecodeError) as error:
            logger.error(f'Invalid or corrupted file: {str(error)}')
            raise error

        except Exception as e:
            logger.error(f'Error by reading file: {str(e)}')
            raise e

class ExistingProcessError:
    """
    Decorator used to disable events generation if another is still running.

    Exceptions:
    -----------
    - psutil.AccessDenied: Process already exists
    """

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """Contains the logic used for the decorator."""
        try:
            for p in psutil.process_iter():
                if p.pid == current_pid:
                    continue

                process_dict: Dict = p.as_dict(attrs=['pid', 'cmdline'])
                pid = process_dict.get('pid')
                cmdline = process_dict.get('cmdline')

                if 'python -m apollo11_simulator generate-events' == ' '.join(cmdline):
                    raise psutil.AccessDenied(
                            msg=f'The event generator is already running with PID: {pid}')
            else:
                self._function(*args, **kwds)

        except psutil.AccessDenied as access_error:
            logger.error(str(access_error))
            exit(-1)
