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
            self.assertIsNotNone(point.building_name, 'building name was None!! :(')

    def test_tags_list_has_only_non_none_vals(self):
        for point in self.decoded_points:
            all_tags = point.get_point_tags() + \
                       point.get_device_tags() + \
                       point.get_building_tags() + \
                       point.get_room_tags()
            for tag in all_tags:
                self.assertIsNotNone(tag, 'tag was set to none!! shame!')


if __name__ == '__main__':
    unittest.main()
