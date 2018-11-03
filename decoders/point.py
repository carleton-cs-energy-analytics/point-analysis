#!/usr/bin/env python3
'''
    point.py
    Chris Tordi, 31 October 2018

    Point Class. Contains data fields and methods relevant to storing and
    updating point data
'''


class Point:

    def __init__(self, point_name):
        self.point_name = point_name
        self.point_desc = "unknown"
        self.building_name = "unknown"
        self.device_name = "unknown"
        self.device_desc = "unknown"
        self.room_name = "unknown"
        self.room_floor = "unknown"
        self.room_desc = "unknown"
        self.units = "unknown"
        self.building_type = "unknown"
        self.device_type = "unknown"
        self.room_type = "unknown"
        self.point_type = "unknown"


    def set_point_name(self, name):
        self.point_name = name

    def get_point_name(self):
        return self.point_name

    def set_point_desc(self, desc):
        self.point_desc = desc

    def get_point_desc(self):
        return self.point_desc

    def set_building_name(self, name):
        self.building_name = name

    def get_building_name(self):
        return self.building_name

    def set_device_name(self, name):
        self.device_name = name

    def get_device_name(self):
        return self.point_name

    def set_device_desc(self, desc):
        self.device_name = desc

    def get_device_desc(self):
        return self.point_desc

    def set_room_name(self, name):
        self.room_name = name

    def get_room_name(self):
        return self.room_name

    def set_room_floor(self, floor):
        self.room_floor = floor

    def get_room_desc(self):
        return self.room_desc

    def set_room_desc(self, desc):
        self.room_desc = desc

    def get_units(self):
        return self.units

    def set_units(self, units):
        self.units = units

    def set_building_type(self, tag):
        self.building_type = tag

    def get_building_type(self):
        return self.building_type

    def set_room_type(self, tag):
        self.room_type = tag

    def get_room_type(self):
        return self.room_type

    def set_device_type(self, tag):
        self.device_type = tag

    def get_device_type(self):
        return self.device_type

    def set_point_type(self, tag):
        self.point_type = tag

    def get_point_type(self):
        return self.point_type

    def get_tags(self):
        return [self.building_type, self.device_type, self.room_type, self.point_type]