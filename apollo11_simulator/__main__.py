from apollo11_simulator.models.event_processing.event_manager import EventManager
from apollo11_simulator.models.report_processing.report_builder import ReportBuilder

#logica argparse
#si es en modo generador
event_manager = EventManager(target_path = 'devices', frequency_seconds = 3, range_of_files = (7, 10))
event_manager()

#si es en modo reporter

#reporter method
#reporter = ReportBuilder.from_path('')
#reporter.show_reporter()
