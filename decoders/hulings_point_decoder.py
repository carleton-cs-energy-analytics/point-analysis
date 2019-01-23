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

    @staticmethod
    def decode_building_name(attr_dict):
        return "Hulings"

    @staticmethod
    def decode_device_name(attr_dict):
        return "unknown"

    @staticmethod
    def decode_device_desc(attr_dict):
        return "unknown"

    @staticmethod
    def decode_room_name(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "RM" in split1:
            return re.findall(r'\d+', split1)
        return "unknown"

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "RM" in split1:
            return re.findall(r'(?<=\D)\d', split1)
        return "unknown"

    @staticmethod
    def decode_units(attr_dict):
        return "unknown"

    @staticmethod
    def decode_building_type(attr_dict):
        return "academic"

    @staticmethod
    def decode_device_type(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split2 = sub_names[2]
        if "DSET" in split2:
            return "Differential Set"
        elif "EDMP" in split2:
            return "Exhaust Damper"
        elif "ESET" in split2:
            return "Exhaust Set"
        elif "EXCFM" in split2:
            return "Exhaust Cubic Feet per Minute"
        elif "EXSET" in split2:
            return "Exhaust Set"
        elif "FCFM" in split2:
            return "Fume Cubic Feet per Minute"
        elif "FDIFF" in split2:
            return "Flow Diff"
        elif "RM" in split2:
            return "Room Temperature"
        elif "RM" in split2:
            return "Room Temperature"
        elif "RSET" in split2:
            return "Room Set Point"
