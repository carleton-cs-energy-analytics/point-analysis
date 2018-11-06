from decoders.point_decoder import PointDecoder
from decoders.point import Point


class HulingsPointDecoder(PointDecoder):

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
        self.point.set_building_name("Hulings")

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
        self.point.set_point_desc("unknown")
