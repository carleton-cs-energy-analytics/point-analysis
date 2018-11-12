from .point import Point


class PointDecoder:
    @staticmethod
    def decode_point_name(attr_dict):
        return attr_dict["Point Name"][0]

    @staticmethod
    def decode_point_desc(attr_dict):
        return "unknown"

    @staticmethod
    def decode_building_name(attr_dict):
        return "unknown"

    @staticmethod
    def decode_device_name(attr_dict):
        return "unknown"

    @staticmethod
    def decode_device_desc(attr_dict):
        return "unknown"

    @staticmethod
    def decode_room_name(attr_dict):
        return "unknown"

    @staticmethod
    def decode_room_floor(attr_dict):
        return "unknown"

    @staticmethod
    def decode_room_desc(attr_dict):
        return "unknown"

    @staticmethod
    def decode_units(attr_dict):
        return "unknown"

    @staticmethod
    def decode_building_type(attr_dict):
        return "unknown"

    @staticmethod
    def decode_device_type(attr_dict):
        return "unknown"

    @staticmethod
    def decode_room_type(attr_dict):
        return "unknown"

    @staticmethod
    def decode_point_type(attr_dict):
        return "unknown"