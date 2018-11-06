#!/usr/bin/env python3
'''
    siemens_master.py
    Ethan Cassel-Mace and Chris Tordi, 4 November 2018

    Controls decoding of Siemens points. Delegates which building subclass a point will be passed to. Outputs list
    of point objects.
'''

from decoders.evans_point_decoder import EvansPointDecoder
from decoders.point_decoder import PointDecoder
import json

# maps building prefixes to building subclass decoders
subClassMap = {'EV': EvansPointDecoder,
               'EVANS': EvansPointDecoder}  # TODO add building mappings as they are discovered and implemented


def get_point_object(name, point):
    '''
    :param name: point name
    :param point: attribute dictionary for point
    :return: Point object
    '''
    prefix = get_prefix(name)   # get prefix of point name
    building_decoder_class = get_building_decoder(prefix)   # class that corresponds to building mapping
    building_decoder = building_decoder_class(point)    # instance of class
    return building_decoder.get_point()


def get_building_decoder(prefix):
    '''
    :param prefix: prefix of point name
    :return:  name of subclass that corresponds to the building of a given point prefix
    '''
    return subClassMap.get(prefix, PointDecoder)


def get_prefix(point_name):
    '''
    :param point_name: name of point
    :return: Prefix of point name. These are calculated as follows:
    if a point has a delimiter, the prefix is the name up to the delimiter. Else, it is
    the first two characters of the point name. '''
    delimiters = {'.', ':', ' ', '-'}
    # calculate index of first delimiter, else None
    first_delimiter_index = next((i for i, ch in enumerate(point_name) if ch in delimiters), None)
    return point_name[:first_delimiter_index] if first_delimiter_index else point_name[:2]


if __name__ == '__main__':
    with open('../data/points.json') as f:
        points = json.loads(f.read())       # read point dictionary from points.json

    point_list = [get_point_object(name, point) for name, point in points.items()]  # list of point objects

    for point in point_list:
        print(str(point))
        pass


    print(' Number of points to decode:', len(points))
    print(' Number of points decoded (attempted):', len(point_list))
    print('================ Decoded points (attempted) ================')
