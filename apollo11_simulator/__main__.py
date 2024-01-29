"""Entrypoint of the application."""

import argparse

from apollo11_simulator.common import Logger
from apollo11_simulator.config import config
from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

logger = Logger.get_logger("__main__")

if __name__ == '__main__':

    event_params = config["event_params"]

    parser = argparse.ArgumentParser(
        description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation',
                        choices = ['generate-events', 'generate-report'],
                        help = 'Tipo de operación: Generar eventos, Generar reportes')

    args = parser.parse_args()

    match args.operation:
        case 'generate-events':
            logger.info('Running in "generate events" mode')

            event_manager = EventManager(
                input_data_file = event_params["input_data_file"],
                devices_path = event_params["devices_path"],
                frequency_seconds = event_params["frequency_seconds"],
                range_of_files = (event_params["range_of_files"]["min"],
                                  event_params["range_of_files"]["max"])
            )

            event_manager()

        case 'generate-report':
            logger.info('Running in "generate report" mode')
            reporter = ReportBuilder.read_events(
                devices_path=event_params["devices_path"],
                backup_path=event_params["backup_path"]
            )

            reporter()
