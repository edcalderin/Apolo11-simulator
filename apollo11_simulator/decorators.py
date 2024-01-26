from json import JSONDecodeError
from typing import Any, Callable
from yaml import YAMLError
from apollo11_simulator.config.logger import Logger

logger = Logger.get_logger("decorators")

class CatchFileExceptions:
    '''
    Decorator used to catch exceptions by reading yaml or json files.

    Exceptions:
    -----------
    - JSONDecodeError: Invalid json file
    - YAMLError: Invalid yaml file
    - Exception: Error by reading file
    '''

    def __init__(self, function: Callable) -> None:
        self._function = function

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        try:
            return self._function(*args, **kwds)

        except (YAMLError, JSONDecodeError) as error:
            logger.error(f'Invalid or corrupted file: {str(error)}')
            raise error

        except Exception as e:
            logger.error(f'Error by reading file: {str(e)}')
            raise e
