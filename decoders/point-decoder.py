
import sys
import os
import csv
import json
from .point import Point


class PointDecoder:

    def __init__(self):
        pass
    
    def get_point(self, attr_dict):
        self.point = Point(attr_dict['Point Name'][0])
        self._set_building()
        self._set_device()
        self._set_room()
        self._set_tags()
        self._set_point_desc()
        self._set_units()

    def _set_building(self):
        self.point.set_building_name("unknown")

    def _set_room(self):
        self.point.set_room_name("unknown")
        self.point.set_room_floor("unknown")
        self.point.set_room_desc("unknown")

    def _set_device(self):
        self.point.set_device_name("unknown")
        self.point.set_device_desc("unknown")

    def _set_units(self):
        self.point.set_units("unknown")

    def _set_tags(self):
        self.point.set_building_type("unknown")
        self.point.set_device_type("unknown")
        self.point.set_room_type("unknown")
        self.point.set_point_type("unknown")

    def _set_point_desc(self):
        self._set_point_desc("unknown")






















if __name__ == '__main__':
    points = {}
    with open('../data/points.json') as f:
        points = json.loads(f.read())
    print('Number of distinct points: {0}'.format(len(points)))
    print()
    print(points)
    print(name)
    for name, values in points:
        PointDecoder.get_point(values)


