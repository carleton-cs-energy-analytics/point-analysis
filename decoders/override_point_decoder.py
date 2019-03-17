import re

from decoders.point_decoder import PointDecoder


class OverridePointDecoder(PointDecoder):
    """
    A point decoder that is applied to points in the override point set in siemens master.
    This is useful for when you want to decode points who's building has not fully been decoded
    """

    @staticmethod
    def decode_point_type(attr_dict):
        name = PointDecoder.decode_point_name(attr_dict)
        type_map = {'STHS.HWRT': 'Hot Water Return',
                    'STHS.HWST': 'Hot Water Supply',
                    'SEV.HX1.HW': 'Hot Water Supply',  # unknown, check back
                    'MCHWRT': 'Hot Water Return',
                    'MCHWST': 'Hot Water Supply',
                    'EV.HX2.HWR': 'Hot Water Return',
                    'SHHWRT': 'Hot Water Return',
                    'SHHWST': 'Hot Water Supply'}

        return type_map.get(name)