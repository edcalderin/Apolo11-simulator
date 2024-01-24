import argparse

from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

# logica argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generador de eventos y reportes en la línea de comandos.')

    parser.add_argument('operation', choices=['generate-events', 'generate-report'],
                        help='Tipo de operacion a realizar: generar eventos, generar reportes')

    args = parser.parse_args()

    match args.operation:
        case 'generate-events':
            print('Running in "generate events" mode')

            event_manager = EventManager(input_data_file = 'input_data/simulation.json',
                                         target_path = 'devices',
                                         frequency_seconds = 3,
                                         range_of_files = (2, 4))
            event_manager()

        case 'generate-report':
            print('Running in "generate report" mode')

            reporter = ReportBuilder.read_events('devices')
            reporter.show_report()
