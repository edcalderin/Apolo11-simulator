# from apollo11_simulator.utils import Utils
from pathlib import Path
from typing import Dict

import yaml

parent_dir = Path(__file__).parent

# config = Utils.read_yaml(parent_dir.joinpath("config.yaml"))

with open(parent_dir.joinpath("config.yaml")) as file:
    config: Dict = yaml.safe_load(file)
