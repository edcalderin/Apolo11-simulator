from unittest import TestCase

from apollo11_simulator.models.event_processing.device import Device
from apollo11_simulator.models.event_processing.device_status import DeviceStatus


# class GenerateHashTest(TestCase):

#     def test_generate_hash_galaxy_two(self):
#         hash_expected = "45996c6220dce5499a6ceb263e31068757a16d46c0a53f7160c1f2f34bee9a77"

#         device: Device = Device(
#             id="1234",
#             device_type="nave",
#             device_status=DeviceStatus.GOOD,
#             device_age=1
#         )

#         hash_obtained = device.get_hash("12122023102202", "GalaxyTwo")

#         self.assertEqual(hash_obtained, hash_expected)
