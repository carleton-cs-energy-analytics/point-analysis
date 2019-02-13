from decoders.point_decoder import PointDecoder
from decoders.point import Point

import re


class HulingsPointDecoder(PointDecoder):

    @staticmethod
    def decode_building_name(attr_dict):
        return "Hulings"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "RM" in split1:
            return re.findall(r'\d+', split1)
        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "RM" in split1:
            return re.findall(r'(?<=\D)\d', split1)
        return None

    @staticmethod
    def decode_building_type(attr_dict):
        return "Academic"

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
