"""
Note: these are not proper unit tests. Instead, they are mostly broad tests that test the entire decoding process,
end to end.
"""

import unittest
from decoders import siemens_master


class PointDecodingTests(unittest.TestCase):

    def setUp(self):
        self.decoded_points = siemens_master.get_points()

    def test_only_returns_decoded_buildings_if_not_override(self):
        for point in self.decoded_points:
            if point.point_name not in siemens_master.OVERRIDE_POINTNAME_SET:
                self.assertIsNotNone(point.building_name, 'building name was None!! :(')

    def test_tags_list_has_only_non_none_vals(self):
        for point in self.decoded_points:
            all_tags = point.get_point_tags() + \
                       point.get_device_tags() + \
                       point.get_building_tags() + \
                       point.get_room_tags()
            for tag in all_tags:
                self.assertIsNotNone(tag, 'tag was set to none!! shame!')

    def test_units_is_correct_format(self):
        for point in self.decoded_points:
            self.assertIn('measurement', point.units)
            self.assertIn('unit', point.units)

    def test_can_get_unit(self):
        for point in self.decoded_points:
            point.get_unit()

    def test_can_get_measurement(self):
        for point in self.decoded_points:
            point.get_measurement()

    def test_floor_is_int_or_none(self):
        for point in self.decoded_points:
            self.assertTrue(isinstance(point.room_floor, (type(None), int)))

    def test_room_is_str_or_none(self):
        for point in self.decoded_points:
            self.assertTrue(isinstance(point.room_name, (type(None), str)))

if __name__ == '__main__':
    unittest.main()
