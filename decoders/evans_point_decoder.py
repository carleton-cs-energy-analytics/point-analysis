import re

from decoders.point_decoder import PointDecoder


class EvansPointDecoder(PointDecoder):
    """
    Decoder for Evans points
    """

    @staticmethod
    def decode_building_name(attr_dict):
        return "Evans"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        name = PointDecoder.decode_point_name(attr_dict)
        # matches EV.RM and then a number, B, or G, then a series of numbers. the last part is the room name
        room_list = re.findall(r'EV\.RM([\dBG]\d+)', name)
        return room_list[0] if room_list else None

    @staticmethod
    def decode_room_floor(attr_dict):
        floor_map = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            'G': 0,
            'B': -1
        }
        name = PointDecoder.decode_point_name(attr_dict)
        # picks out the first character of the room name. See decode_room_name() regex above  for more details
        floor_list = re.findall(r'EV\.RM([\dBG])\d+', name)
        return floor_map.get(floor_list[0], None) if floor_list else None

    @staticmethod
    def decode_building_type(attr_dict):
        return "Residential"

    @staticmethod
    def decode_device_type(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "CUH" in split1:
            return "Cabinet Unit Heater"
        elif "DCP" in split1:
            return "Domestic Circulating Pump"
        elif "FCU" in split1:
            return "Fan Coil Unit"
        elif "HRV" in split1:
            return "Heat Recovery Ventilator"
        elif "HWP" in split1:
            return "Hot Water Pump"
        elif "HX" in split1:
            return "Heat Exchanger"
        elif "FC" in split1:
            return "Fan Coil Unit"
        return None

    @staticmethod
    def decode_point_type(attr_dict):
        name = PointDecoder.decode_point_name(attr_dict)
        sub_names = PointDecoder.get_delimited_pointname(attr_dict)
        if len(sub_names) == 3:
            split2 = sub_names[2]
            if "RT" == split2:
                return "Room Temperature"
            elif "SP" == split2:
                return "Room Temperature Set Point"
            elif "V" == split2:
                return "Radiation Valve"
        if name[-3:] == 'VSP' or name[-8:] == 'VSP cave':
            return "Virtual Room Temperature Set Point"
        if sub_names[-1] == 'DAY HTG STPT':
            return "Day Heating Set Point"
        if sub_names[-1] == 'NGT HTG STPT':
            return "Night Heating Set Point"
        if sub_names[-1] == 'DAY CLG STPT':
            return "Day Cooling Set Point"
        if sub_names[-1] == 'NGT CLG STPT':
            return "Night Cooling Set Point"
        if sub_names[-1] == 'RM STPT DIAL':
            return "Room Set Point Dial"

        return None
