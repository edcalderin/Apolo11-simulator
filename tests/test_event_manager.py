from apollo11_simulator.models.event_processing.event_manager import EventManager

from pydantic import ValidationError
import pytest
from typing import Dict

class TestEventManager:

    '''
    Class to test EventManager class.
    The possible exceptions may be rised by instantiating the class with invalid attributes.

    - target_path: Empty string
    - frequency_sounds: Less than zero
    - range_of_files: Both Values must be positive and different from zero,
    the second value must be greater than the first one.
    '''

    def test_input_data_file(self):
        '''
        Test target_path attribute with an empty string
        '''
        with pytest.raises(ValidationError):
            EventManager(input_data_file = '', devices_path = 'devices', frequency_seconds = 3, range_of_files = (1, 2))

    def test_target_path(self):
        '''
        Test target_path attribute with an empty string
        '''
        with pytest.raises(ValidationError):
            EventManager(devices_path = '', frequency_seconds = 3, range_of_files = (1, 2))

    def test_frequency_sounds(self):
        '''
        Test frequency_sounds attribute with a value less than zero
        '''
        with pytest.raises(ValidationError):
            EventManager(devices_path = 'dir', frequency_seconds = 0, range_of_files = (1, 2))

    def test_range_of_files_gt_1(self, partial_event_manager: Dict):
        '''
        Test range_of_files attribute with negative values
        '''
        with pytest.raises(ValueError, match='All the values must be greater than 1'):
            EventManager(**partial_event_manager, range_of_files = (0, 0))

    def test_range_of_files_consecutive(self, partial_event_manager: Dict):
        '''
        Test range_of_files attribute being the first value greater than the second one
        '''
        with pytest.raises(ValueError, match='The second value must be greater than the first one'):
            EventManager(**partial_event_manager, range_of_files = (2, 1))
