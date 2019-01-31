"""
Note: these are not proper unit tests. Instead, they are mostly broad tests that test the entire decoding process,
end to end.
"""

import unittest
from decoders import siemens_master


class PointDecodingTests(unittest.TestCase):

    def setUp(self):
        self.decoded_points = siemens_master.get_points()

    def test_only_returns_decoded_buildings(self):
        for point in self.decoded_points:
            assert point.building_name is not None


if __name__ == '__main__':
    unittest.main()
