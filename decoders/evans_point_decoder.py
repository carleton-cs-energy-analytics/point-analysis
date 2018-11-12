from decoders.point_decoder import PointDecoder
from .point import Point


class EvansPointDecoder(PointDecoder):

    @staticmethod
    def decode_building_name(attr_dict):
        return "Evans"
