import pytest
from pathlib import Path
from typing import Dict

@pytest.fixture
def test_data_path() -> Path:
    return Path('tests').joinpath('test_data')

@pytest.fixture
def partial_event_manager() -> Dict:
    return {
        'target_path': 'path',
        'frequency_seconds': 3
    }