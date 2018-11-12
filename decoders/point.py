#!/usr/bin/env python3
'''
    point.py
    Chris Tordi, 31 October 2018

    Point Class. Contains data fields and methods relevant to storing and
    updating point data
'''


class Point:

    def __init__(self, attr_dict, decoder):
        self.point_name = decoder.decode_point_name(attr_dict)
        self.point_desc = decoder.decode_point_desc(attr_dict)
        self.building_name = decoder.decode_building_name(attr_dict)
        self.device_name = decoder.decode_device_name(attr_dict)
        self.device_desc = decoder.decode_device_desc(attr_dict)
        self.room_name = decoder.decode_room_name(attr_dict)
        self.room_floor = decoder.decode_room_floor(attr_dict)
        self.room_desc = decoder.decode_room_desc(attr_dict)
        self.units = decoder.decode_units(attr_dict)
        self.building_type = decoder.decode_building_type(attr_dict)
        self.device_type = decoder.decode_device_type(attr_dict)
        self.room_type = decoder.decode_room_type(attr_dict)
        self.point_type = decoder.decode_point_type(attr_dict)


    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        return str(dict(self))

    def get_tags(self):
        return [self.building_type, self.device_type, self.room_type, self.point_type]