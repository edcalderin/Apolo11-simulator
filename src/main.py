from src.models.event_processing.event_manager import EventManager
from src.models.report_processing.report_builder import ReportBuilder

#logica argparse
#si es en modo generador
event_manager = EventManager(frequency_seconds=10, number_of_files=(7, 10))
event_manager()

#si es en modo reporter

#reporter method
#reporter = ReportBuilder.from_path('')
#reporter.show_reporter()
