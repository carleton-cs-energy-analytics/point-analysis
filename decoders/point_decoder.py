

class PointDecoder:
    """
    A set of static methods to decode parts of a point, that can be overridden by sub-classes.
    """
    @staticmethod
    def decode_point_name(attr_dict):
        return attr_dict["Point System Name"][0]

    @staticmethod
    def decode_verbose_point_name(attr_dict):
        return attr_dict["Point Name"][0]

    @staticmethod
    def decode_point_desc(attr_dict):
        return None

    @staticmethod
    def decode_building_name(attr_dict):
        return None

    @staticmethod
    def decode_device_name(attr_dict):
        return None

    @staticmethod
    def decode_device_desc(attr_dict):
        return None

    @staticmethod
    def decode_room_name(attr_dict):
        return None

    @staticmethod
    def decode_room_floor(attr_dict):
        return None

    @staticmethod
    def decode_room_desc(attr_dict):
        return None

    @staticmethod
    def decode_units(attr_dict):
        unit_map = {'DEG F': {'measurement': 'temperature',
                              'unit': 'degrees fahrenheit'},
                    'PCT': {'measurement': 'proportion open',
                            'unit': 'percent'},
                    'PCNT': {'measurement': 'proportion open',
                             'unit': 'percent'},
                    'GAL': {'measurement': 'volume',
                            'unit': 'gallons'},
                    '% clos': {'measurement': 'proportion closed',
                               'unit': 'percent'},
                    '% RH': {'measurement': 'humidity',
                             'unit': 'percent'},
                    '%RH': {'measurement': 'humidity',
                            'unit': 'percent'},
                    'KW': {'measurement': 'energy',
                           'unit': 'kilowatt hours'},
                    'KWH': {'measurement': 'energy',
                            'unit': 'kilowatt hours'},
                    'LBM': {'measurement': 'mass',
                            'unit': 'pounds'},
                    'LBH': {'measurement': 'pounds per unit time',
                            'unit': 'pounds per hour'},
                    'LBM/HR': {'measurement': 'pounds per unit time',
                               'unit': 'pounds per hour'},
                    'HZ': {'measurement': 'frequency',
                           'unit': 'hertz'},
                    'GPM': {'measurement': 'volume per unit time',
                            'unit': 'gallons per minute'},
                    'PSI': {'measurement': 'pressure',
                            'unit': 'pounds per square inch'},
                    'PSID': {'measurement': 'pressure differential',
                             'unit': 'pounds per square inch'},
                    'CFM': {'measurement': 'volume per unit time',
                            'unit': 'cubic feet per minute'},
                    'SQ. FT': {'measurement': 'area',
                               'unit': 'square feet'},
                    'HP': {'measurement': 'power',
                           'unit': 'horsepower'}
                    }

        if 'Engineering Units' in attr_dict:
            return unit_map.get(attr_dict['Engineering Units'][0], {'measurement': None,
                                                                    'unit': None})

        return {'measurement': None,
                'unit': None}

    @staticmethod
    def decode_building_type(attr_dict):
        return None

    @staticmethod
    def decode_device_type(attr_dict):
        return None

    @staticmethod
    def decode_room_type(attr_dict):
        return None

    @staticmethod
    def decode_point_type(attr_dict):
        return None

    @staticmethod
    def decode_value_type(attr_dict):
        if "Text Table" in attr_dict:
            return attr_dict["Text Table"][0]
        elif "Analog Representation" in attr_dict:
            return attr_dict["Analog Representation"][0]
        else:
            return None

    @staticmethod
    def get_delimited_pointname(attr_dict):
        """
        returns a list of all the sections of the point name, split on all the possible delimiters.
        :param attr_dict:
        :return:
        """
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
        wanted_items = ['Engineering Units', 'Classification', 'Panel Name', 'Point Type',
                        'Point Name', 'Descriptor', 'Engineering Units']
        return {k: v for (k, v) in attr_dict.items() if k in wanted_items}
