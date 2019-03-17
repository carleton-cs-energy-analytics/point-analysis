#!/usr/bin/env python3
'''
    point.py
    Chris Tordi & Ethan Cassel-Mace, 31 October 2018

    Point Class. Contains data fields and methods relevant to storing and
    updating point data
'''


class Point:
    """
    A class that represents all the information about a point.
    """

    def __init__(self, attr_dict, decoder):
        """
        :param attr_dict: dict version of point documentation
        :param decoder: decoder class used to decode the point. Either building sub class, or
        generic super class.

        Uses the decoder to decode the attr_dict.
        """
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
        self.value_type = decoder.decode_value_type(attr_dict)

    def __iter__(self):
        """
        :return: iterable version of point. Essentially makes a dict of all the instance variable names
        """
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        return str(dict(self))

    def get_point_tags(self):
        """
        :return: list of all instance variables that will go into the DB as a "point tag"
        """
        point_tags = [self.point_type] # currently point_type is the only tag we decode for a point.
        return [tag for tag in point_tags if tag is not None]

    def get_device_tags(self):
        """
        :return: list of all instance variables that will go into the DB as a "device tag"
        """

        device_tags = [self.device_type]
        return [tag for tag in device_tags if tag is not None]

    def get_room_tags(self):
        """
        :return: list of all instance variables that will go into the DB as a "room tag"
        """
        room_tags = [self.room_type]
        return [tag for tag in room_tags if tag is not None]

    def get_building_tags(self):
        """
        :return: list of all instance variables that will go into the DB as a "building tag"
        """
        building_tags = [self.building_type]
        return [tag for tag in building_tags if tag is not None]

    def get_unit(self):
        """
        convenience method since unit and measurement are decoded together as "units"
        :return: unit of point
        """
        return self.units['unit']

    def get_measurement(self):
        """
        convenience method since unit and measurement are decoded together as "units"
        :return: measurement of point
        """
        return self.units['measurement']
