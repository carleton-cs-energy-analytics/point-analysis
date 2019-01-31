'''
    Miaoye Que, Last Updated Jan 21, 2019
    Decodes point data in Boliou
'''

import re

from decoders.point_decoder import PointDecoder


class BoliouPointDecoder(PointDecoder):

    @staticmethod
    def decode_building_name(attr_dict):
        return "Boliou"

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        sub_names = attr_dict["Point Name"][0].split(':')
        location_name = sub_names[0]
        location_units = location_name.split('.')
        if len(location_units) == 4:
            room_name = location_units[3]
            if "RM" in room_name:
                room_name_list = re.findall(r'\d+', room_name)
                return room_name_list[0] if room_name_list else None
        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"][0].split(':')
        split0 = sub_names[0]
        if ".1." in split0:
            return "First"
        elif "FIRST" in split0:
            return "First"
        elif "GND" in split0:
            return "Ground"
        return None

    @staticmethod
    def decode_units(attr_dict):
        unit_map = {
            'CFM': 'cubic feet per minute',
            'DEG F': 'degrees fahrenheit',
            'PCT': 'percent open',
            'SQ. FT': 'square feet'}

        if 'Engineering Unit' in attr_dict:
            return unit_map.get(attr_dict['Engineering Units'][0])

        return None

    @staticmethod
    def decode_building_type(attr_dict):
        return "Academic"

    @staticmethod
    def decode_point_type(attr_dict):
        sub_names = attr_dict["Point Name"][0].split(':')
        split1 = sub_names[1]
        if "AIR VOLUME" in split1:
            return "Air Volume"
        elif "AUX TEMP" in split1:
            return "Aux Temperature"
        elif "CLG FLOW MAX" in split1:
            return "Cooling Maximum Flow"
        elif "CLG FLOW MIN" in split1:
            return "Cooling Minimum Flow"
        elif "CLG LOOPOUT" in split1:
            return "Cooling Loopout"
        elif "CTL FLOW MAX" in split1:
            return "Controller Maximum Flow"
        elif "CTL FLOW MIN" in split1:
            return "Controller Minimum Flow"
        elif "CTL STPT" in split1:
            return "Controller Setpoint"
        elif "CTL TEMP" in split1:
            return "Controller Temperature"
        elif "DAY CLG STPT" in split1:
            return "Day Cooling Setpoint"
        elif "DAY HTG STPT" in split1:
            return "Day Heating Setpoint"
        elif "DAY.NGT" in split1:
            return "Day/Night"
        elif "DMPR COMD" in split1:
            return "Damper Command"
        elif "DMPR POS" in split1:
            return "Damper Position"
        elif "DUCT AREA" in split1:
            return "Duct Area"
        elif "FLOW COEFF" in split1:
            return "Flow Coefficient"
        elif "FLOW STPT" in split1:
            return "Flow Setpoint"
        elif "FLOW" in split1:
            return "Flow"
        elif "HEAT.COOL" in split1:
            return "Heating/Cooling"
        elif "HTG FLOW MAX" in split1:
            return "Heating Maximum Flow"
        elif "HTG FLOW MIN" in split1:
            return "Heating Minimum Flow"
        elif "HTG LOOPOUT" in split1:
            return "Heating Loopout"
        elif "MTR SETUP" in split1:
            return "Meter Setup"
        elif "NGT CLG STPT" in split1:
            return "Night Cooling Setpoint"
        elif "NGT HTG STPT" in split1:
            return "Night Heating Setpoint"
        elif "NGT OVRD" in split1:
            return "Night Override"
        elif "ROOM TEMP" in split1:
            return "Room Temperature"
        elif "VALVE COUNT" in split1:
            return "Valve Count"
        elif "VLV1 COMD" in split1:
            return "Valve One Command"
        elif "VLV1 POS" in split1:
            return "Valve One Position"
        elif "VLV2 COMD" in split1:
            return "Valve Two Command"
        elif "VLV2 POS" in split1:
            return "Valve Two Position"
        return None
