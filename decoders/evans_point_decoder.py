import re

from decoders.point_decoder import PointDecoder


class EvansPointDecoder(PointDecoder):

    @staticmethod
    def decode_building_name(attr_dict):
        return "Evans"

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
            room_name_list = re.findall(r'\d+', split1)
            return room_name_list[0] if room_name_list else 'unknown'
        return "unknown"

    @staticmethod
    def decode_room_floor(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        split1 = sub_names[1]
        if "RM" in split1:
            room_floor_list =  re.findall(r'(?<=\D)\d', split1)
            return room_floor_list[0] if room_floor_list else 'unknown'
        return "unknown"

    @staticmethod
    def decode_units(attr_dict):
        unit_map = {'DEG F': 'degrees fahrenheit',
                    'PCT': 'percent open',
                    'PCNT': 'percent open',
                    'GAL': 'gallons',
                    '% clos': 'percent closed',
                    '% RH': 'percent humidity',
                    '%RH': 'percent humidity',
                    'KW': 'kilowatt hours',
                    'KWH': 'kilowatt hours',
                    'LBM': 'pounds',                # These steam measurements are relative guesses
                    'LBH': 'pounds per hour',
                    'LBM/HR': 'pounds per hour',
                    'HZ': 'hertz',
                    'GPM': 'gallons per minute',
                    'PSI': 'pressure per square inch',
                    'PSID': 'pressure differential',
                    'CFM': 'cubic feet per minute', }

        if 'Engineering Units' in attr_dict:
            return unit_map.get(attr_dict['Engineering Units'][0], 'unknown')

        return "unknown"

    @staticmethod
    def decode_building_type(attr_dict):
        return "residential"

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
        return "unknown"

    @staticmethod
    def decode_point_type(attr_dict):
        sub_names = attr_dict["Point Name"][0].split('.')
        if len(sub_names) == 3:
            split2 = sub_names[2]
            if "RT" in split2:
                return "Room Temperature"
            elif "SP" in split2:
                return "Room Temperature Set Point"
            elif "V" in split2:
                return "Radiation Valve"
        return "unknown"
