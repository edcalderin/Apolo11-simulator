import pytest
from pathlib import Path

@pytest.fixture
def test_data_path() -> Path:
    return Path('tests').joinpath('test_data')