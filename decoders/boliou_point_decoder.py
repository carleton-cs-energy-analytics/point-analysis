'''
    Miaoye Que, Last Updated Jan 16, 2019
    Decodes point data in Boliou
'''

from decoders.point_decoder import PointDecoder

class BoliouPointDecoder(PointDecoder):

    @staticmethod
    def decode_building_name(attr_dict):
        return "Boliou"

    @staticmethod
    def decode_device_name(attr_dict):
        return "unknown"

    @staticmethod
    def decode_device_desc(attr_dict):
        return "unknown"

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
        elif "FLOW COEFF" in split1:
            return "Flow Coefficient"
        elif "FLOW STPT" in split1:
            return "Flow Setpoint"
        elif "FLOW" in split1:
            return "Flow"
        elif "HTG FLOW MAX" in split1:
            return "Heating Maximum Flow"
        elif "HTG FLOW MIN" in split1:
            return "Heating Minimum Flow"
        elif "HTG LOOPOUT" in split1:
            return "Heating Loopout"
        return "unknown"