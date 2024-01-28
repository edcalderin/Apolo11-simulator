from pathlib import Path
from typing import Dict

import yaml

parent_dir = Path(__file__).parent

with open(parent_dir.joinpath('config.yaml')) as file:
    config: Dict = yaml.safe_load(file)
