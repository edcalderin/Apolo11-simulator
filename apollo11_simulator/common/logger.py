import logging
from datetime import datetime
from logging import handlers
from pathlib import Path

from apollo11_simulator.config import config


class Logger:

    @staticmethod
    def get_logger(
        module_name: str,
        log_location: str = config["logging"]["log_location"],
        log_format: str = config["logging"]["log_format"],
        logger_level: int = config["logging"]["logger_level"],
    ):
        '''
        Custom logger to use in the app

        Parameters:
        ----------
        - module_name: name of the application or floe that is running
        - logger_level: logger level - CRITICAL=50,
        ERROR=40, WARNING=30, INFO=20, DEBUG=10, NOTSET=0
        '''

        log_path: Path = Path(log_location)
        log_path.mkdir(exist_ok = True)
        log_save = log_path.joinpath(
            f'{datetime.now().strftime(log_format)}_{module_name}.log'
        )

        logger = None
        try:
            logger = logging.getLogger(module_name)
            logger.setLevel(logger_level)

            format = logging.Formatter(config["logging"]["message_format"])
            login_stream_handler = logging.StreamHandler()
            login_stream_handler.setFormatter(format)
            logger.addHandler(login_stream_handler)

            file_handler = handlers.RotatingFileHandler(log_save,
                                                        maxBytes = (1048576 * 5),
                                                        backupCount = 7
            )
            file_handler.setFormatter(format)
            logger.addHandler(file_handler)

        except Exception:
            logger = None

        return logger
