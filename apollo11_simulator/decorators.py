from json import JSONDecodeError
from typing import Any, Callable

from yaml import YAMLError

from apollo11_simulator.common import Logger

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
