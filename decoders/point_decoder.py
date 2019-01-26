

class PointDecoder:
    @staticmethod
    def decode_point_name(attr_dict):
        return attr_dict["Point System Name"][0]

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

    @staticmethod
    def decode_value_type(attr_dict):
        if attr_dict.get("Text Table") is not None:
            return attr_dict.get("Text Table")[0]
        elif attr_dict.get("Analog Representation") is not None:
            return attr_dict.get("Analog Representation")[0]
        else:
            return "unknown"

    @staticmethod
    def get_delimited_pointname(attr_dict):
        name = PointDecoder.decode_point_name(attr_dict)
        simplified_name = name.replace(';', '.').replace(':', '.').replace('-', '.')
        return simplified_name.split('.')

    @staticmethod
    def get_useful_attr_dict(attr_dict):
        """
        Helper method for print statements to avoid unnecessarily verbose printouts
        :param attr_dict: attribute dictionary
        :return: simplified attribute dict, with only usually useful values
        """
        wanted_items = ['Engineering Units', 'Classification', 'Panel Name', 'Point Type', 'Point Name', 'Descriptor', 'Engineering Units']
        return {k: v for (k, v) in attr_dict.items() if k in wanted_items}
