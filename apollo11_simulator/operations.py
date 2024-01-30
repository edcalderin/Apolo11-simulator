from typing import Dict

from apollo11_simulator.common import Logger
from apollo11_simulator.decorators import ExistingProcessError
from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

logger = Logger.get_logger('operations')

class ArgParseOperations:
    """Operations for ArgParse."""

    def __init__(self, event_params: Dict) -> None:
        """Initialize the class object.

        Args:
            event_params (Dict): Dictionary with params.
        """
        self._event_params = event_params

    @ExistingProcessError
    def generate_events(self):
        """Generate events operation."""
        logger.info('Running in "generate events" mode')

        event_manager = EventManager(
            input_data_file = self._event_params["input_data_file"],
            devices_path = self._event_params["devices_path"],
            frequency_seconds = self._event_params["frequency_seconds"],
            range_of_files = (self._event_params["range_of_files"]["min"],
                                self._event_params["range_of_files"]["max"])
        )

        event_manager()

    def generate_report(self) -> None:
        """Generate report operation."""
        logger.info('Running in "generate report" mode')

        reporter = ReportBuilder.read_events(
            devices_path = self._event_params["devices_path"],
            backup_path = self._event_params["backup_path"]
        )

        reporter()
