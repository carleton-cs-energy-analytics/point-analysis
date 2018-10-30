#!/usr/bin/env python3
'''
    point-analyzer.py
    Jeff Ondich, 20 October 2018
    Chris Tordi, 22 October 2018
    Ethan Cassel-Mace, 24 October 2018

    Miscellaneous operations performed on Carleton's Siemens point data,
    as stored to JSON by definitions2json.py
'''

import sys
import os
import csv
import json


def point_names(points):
    return sorted(points.keys())


def point_name_prefixes(points, n=None, as_dict=False):
    ''' Returns a collection of points, as specified by optional parameters
        :param points: dict of points to parse
        :param n: size of prefix. If omitted, prefixes are calculated up to a .
        :param as_dict:  True, if result should be dict rather than sorted list of tuples
        :return: sorted list of tuples of (prefix, count) if as_dict is False,
                dict of prefix : count if as_dict is True. '''
    prefixes = {}
    for name in points:
        index = n if n else name.find('.')
        if index >= 0:
            prefix = name[:index]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
    return prefixes if as_dict else sorted(prefixes.items(), key=lambda x: (x[1], x[0]), reverse=True)


def point_name_smart_prefixes(points, as_dict=False):
    ''' :param points: dict of points
        :param as_dict: True, if result should be dict rather than sorted list of tuples
        :return: Collection of point prefixes and counts. These are calculated as follows:
         if a point has a delimiter, the prefix is the name up to the delimiter. Else, it is
         the first two characters of the point name. '''
    prefixes = {}
    for name in points:
        prefix = get_point_name_smart_prefix(points[name])
        prefixes[prefix] = prefixes.get(prefix, 0) + 1
    return prefixes if as_dict else sorted(prefixes.items(), key=lambda x: (x[1], x[0]), reverse=True)


def get_point_name_smart_prefix(point):
    name = point['Point System Name'][0]
    delimiters = {'.', ':', ' ', '-'}
    # calculate index of first delimiter, else None
    first_delimiter_index = next((i for i, ch in enumerate(name) if ch in delimiters), None)
    return name[:first_delimiter_index] if first_delimiter_index else name[:2]


def filter_points(points, predicate):
    ''' filters points based on some predicate function
        :param points: dict of points
        :param predicate: predicate function to filter on. Should accept a single point as a param
        :return: filtered version of points, only with points p for which predicate(p) is True '''
    return {k: v for (k, v) in points.items() if predicate(v)}


def is_thermostat_point(point):
    ''' predicate for checking whether a point is thermostat related
        :param point: a point in dict form
        :return: True, if and only if the point is a thermostat point '''
    components_of_name = ['STPT', 'STP', 'ROOM TEMP', 'RMT']
    return any(component in point['Point System Name'][0] for component in components_of_name)


def is_non_delimited_point(point):
    return is_non_dot_delimited_point(point) and \
           is_non_colon_delimited_point(point) and \
           is_non_dash_delimited_point(point) and \
           is_non_space_delimited_point(point)


def is_non_dot_delimited_point(point):
    return '.' not in point['Point System Name'][0]


def is_non_colon_delimited_point(point):
    return ':' not in point['Point System Name'][0]


def is_non_dash_delimited_point(point):
    return '-' not in point['Point System Name'][0]


def is_non_space_delimited_point(point):
    return ' ' not in point['Point System Name'][0]


def is_hulings_point(point):
    hulings_prefixes = ['HU', 'BO', 'HULINGS', 'HULLINGS']
    return any(component == point['Point System Name'][0][:len(component)] for component in hulings_prefixes)


def is_weitz_point(point):
    weitz_prefixes = ['WC', 'WCC']
    return any(component == point['Point System Name'][0][:len(component)] for component in weitz_prefixes)


if __name__ == '__main__':
    with open('../data/points.json') as f:
        points = json.loads(f.read())

    prefixes_first_three = point_name_prefixes(points, 3)
    prefixes_dict_first_three = point_name_prefixes(points, n=3, as_dict=True)
    first_component_prefixes = point_name_prefixes(points)
    first_component_prefixes_dict = point_name_prefixes(points, as_dict=True)

    thermostat_points = filter_points(points, is_thermostat_point)
    thermostat_prefixes = point_name_prefixes(thermostat_points)
    thermostat_prefixes_dict = point_name_prefixes(thermostat_points, as_dict=True)

    non_dot_delimited_points = filter_points(points, is_non_dot_delimited_point)
    non_delimited_points = filter_points(points, is_non_delimited_point)

    print('Number of distinct points: {0}'.format(len(points)))
    print('Number of distinct thermostat points: {0}'.format(len(thermostat_points)))
    print('Number of points delimited with a . : {0}'.format(len(points) - len(non_dot_delimited_points)))
    print('Number of points NOT delimited with a . : {0}'.format(len(non_dot_delimited_points)))
    print('Number of completely non deliminated points: {0}'.format(len(non_delimited_points)))
    print()

    print('========== non . delimited point names ==========')
    non_delimited_point_names = sorted([points[point]['Point System Name'][0] for point in non_dot_delimited_points])
    for name in non_delimited_point_names:
        # print(name)
        pass  # to allow commenting out print statement above

    print('========== 3-letter prefixes ==========')
    for prefix, count in prefixes_first_three:
        # print(prefix, count)
        pass  # to allow commenting out print statement above
    print()

    print('========== prefixes up to first . ==========')
    for prefix, count in first_component_prefixes:
        # print(prefix, count)
        pass  # to allow commenting out print statement above

    print('========== 3-letter prefixes of thermostat points ==========')
    for prefix, count in thermostat_prefixes:
        # print(prefix, count)
        pass  # to allow commenting out print statement above
    print()

    print('========== prefixes not present in thermostat points ==========')
    prefix_diff_dict = {k: v for (k, v) in first_component_prefixes_dict.items() if k not in thermostat_prefixes_dict}
    prefix_diff_sorted = sorted(prefix_diff_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)
    for prefix, count in prefix_diff_sorted:
        print(prefix, count)
        pass  # to allow commenting out print statement above

    print('========== non-delimited point names ==========')
    for point_name in sorted(non_delimited_points.keys()):
        # print(point_name)
        pass  # to allow commenting out print statement above

    print('========== Point name "smart" prefixes (first delimiter or 2 chars) ==========')
    smart_prefixes = point_name_smart_prefixes(points)
    for prefix, count in smart_prefixes:
        print(prefix, count)
