"""Entrypoint of the application."""

import argparse
from typing import Dict

from apollo11_simulator.common import Logger
from apollo11_simulator.config import config
from apollo11_simulator.operations import Operations

logger = Logger.get_logger("__main__")

if __name__ == '__main__':

    event_params: Dict = config["event_params"]

    parser = argparse.ArgumentParser(
        description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation',
                        choices = ['generate-events', 'generate-report'],
                        help = 'Tipo de operación: Generar eventos, Generar reportes')

    args = parser.parse_args()

    operations_ = Operations(event_params)

    match args.operation:
        case 'generate-events':
            operations_.generate_events()

        case 'generate-report':
            operations_.generate_report()
