from json import JSONDecodeError
from typing import Any, Callable
from yaml import YAMLError

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
            print(f'Invalid or corrupted file: {str(error)}')
            raise error

        except Exception as e:
            print(f'Error by reading file: {str(e)}')
            raise e
