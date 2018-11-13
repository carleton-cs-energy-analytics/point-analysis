from decoders.point_decoder import PointDecoder
from .point import Point
import re


class EvansPointDecoder(PointDecoder):
    pass

    def __init__(self, attr_dict):
        self.point = Point(attr_dict['Point Name'][0])
        self.attr_dict = attr_dict

        self._set_building()
        self._set_device()
        self._set_room()
        self._set_tags()
        self._set_point_desc()
        self._set_units()



    def get_point(self):
        return self.point

    def _set_building(self):
        self.point.set_building_name("Evans")

    def _set_room(self):
        split = self.split_name(self.point.point_name)
        split1 = split[1]
        if "RM" in split1:
            number = re.findall(r'\d+', split1)
            self.point.set_room_name(number)
            floor = re.findall(r'(?<=\D)\d', split1)
            self.point.set_room_floor(floor)
        else:
            self.point.set_room_name("unknown")
            self.point.set_room_floor("unknown")
        self.point.set_room_desc("unknown")

    def _set_device(self):
        split = self.split_name(self.point.point_name)
        split1 = split[1]
        if "CUH" in split1:
            self.point.set_device_name("Cabinet Unit Heater")
        elif "DCP" in split1:
            self.point.set_device_name("Domestic Circulating Pump")
        elif "FCU" in split1:
            self.point.set_device_name("Fan Coil Unit")
        elif "HRV" in split1:
            self.point.set_device_name("Heat Recovery Ventilator")
        elif "HWP" in split1:
            self.point.set_device_name("Hot Water Pump")
        elif "HX" in split1:
            self.point.set_device_name("Heat Exchanger")
        elif "FC" in split1:
            self.point.set_device_name("Fan Coil Units")
        else:
            self.point.set_device_name("unknown")
        self.point.set_device_desc("unknown")

    def _set_units(self):
        self.point.set_units("unknown")

    def _set_tags(self):
        split = self.split_name(self.point.point_name)
        split1 = split[1]
        if len(split) == 3:
            split2 = split[2]
            if "RT" in split2:
                self.point.set_point_type("Room Temperature")
            elif "SP" in split2:
                self.point.set_point_type("Room Temperature Set Point")
            elif "V" in split2:
                self.point.set_point_type("Radiation Valve")
            else:
                self.point.set_point_type("unknown")
        else:
            self.point.set_point_type("unknown")

        self.point.set_building_type("Residential")
        self.point.set_device_type("unknown")
        if "RMG" in split1:
            self.point.set_room_type("Ground Room")
        elif "RMB" in split1:
            self.point.set_room_type("Basement Room")
        elif "RM" in split1:
            self.point.set_room_type("Room")
        else:
            self.point.set_room_type("unknown")



    def _set_point_desc(self):
        self.point.set_point_desc("unknown")

    def split_name(self, point_name):
        sub_names = point_name.split('.')
        return sub_names

