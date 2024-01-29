from typing import Dict

from apollo11_simulator.common import Logger
from apollo11_simulator.decorators import ExistingProcessError
from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

logger = Logger.get_logger('operations')

class ArgParseOperations:

    @staticmethod
    @ExistingProcessError
    def generate_events(event_params: Dict):
        logger.info('Running in "generate events" mode')

        event_manager = EventManager(
            input_data_file = event_params["input_data_file"],
            devices_path = event_params["devices_path"],
            frequency_seconds = event_params["frequency_seconds"],
            range_of_files = (event_params["range_of_files"]["min"],
                                event_params["range_of_files"]["max"])
        )

        event_manager()

    @staticmethod
    def generate_report(event_params: Dict) -> None:
        logger.info('Running in "generate report" mode')

        reporter = ReportBuilder.read_events(
            devices_path = event_params["devices_path"],
            backup_path = event_params["backup_path"]
        )

        reporter()
