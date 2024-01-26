from apollo11_simulator.utils import Utils
from pathlib import Path

parent_dir = Path(__file__).parent

config = Utils.read_yaml(parent_dir.joinpath("config.yaml"))