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
        self.building_tags = []
        self.device_tags = []
        self.room_tags = []
        self.point_tags = []

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

    def set_building_tags(self, tags):
        self.building_tags = tags

    def get_building_tags(self):
        return self.building_tags

    def set_device_tags(self, tags):
        self.device_tags = tags

    def get_device_tags(self):
        return self.building_tags

    def set_room_tags(self, tags):
        self.room_tags = tags

    def get_room_tags(self):
        return self.room_tags

    def set_point_tags(self, tags):
        self.point_tags = tags

    def get_point_tags(self):
        return self.point_tags




