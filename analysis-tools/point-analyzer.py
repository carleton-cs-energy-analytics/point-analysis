#!/usr/bin/env python3
'''
    point-analyzer.py
    Jeff Ondich, 20 October 2018

    Miscellaneous operations performed on Carleton's Siemens point data,
    as stored to JSON by definitions2json.py
'''

import sys
import os
import csv
import json

def point_names(points):
    return sorted(points.keys())

def point_name_prefixes(points, n):
    ''' Computes a list of the n-character prefixes of the point names. Returns
        a list of (prefix, count) 2-tuples (where count is the number of points
        whose names start with prefix), sorted in decreasing order by count. '''
    prefixes = {}
    for name in points:
        prefix = name[:n]
        prefixes[prefix] = prefixes.get(prefix, 0) + 1
    return sorted(prefixes.items(), key=lambda x: (x[1], x[0]), reverse=True)

def point_names_without_dots_prefixes(points, n):
    ''' Computes a list of the n-character prefixes of the point names that do not have punctuation. Returns
        a list of (prefix, count) 2-tuples (where count is the number of points
        whose names start with prefix), sorted in decreasing order by count. '''
    prefixes = {}
    for name in points:
        if "." not in name:
            prefix = name[:n]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
    return sorted(prefixes.items(), key=lambda x: (x[1], x[0]), reverse=True)


def point_name_first_components(points):
    ''' Computes a list of the prefixes up to the first period in each point name.
        If a point does not include a period, then its name is not included in
        the returned results. Returns a list of (prefix, count) 2-tuples
        (where count is the number of points whose names start with prefix),
        sorted in decreasing order by count. '''
    prefixes = {}
    for name in points:
        index = name.find('.')
        if index >= 0:
            prefix = name[:index]
            prefixes[prefix] = prefixes.get(prefix, 0) + 1
    return sorted(prefixes.items(), key=lambda x: (x[1], x[0]), reverse=True)

if __name__ == '__main__':
    points = {}
    with open('points.json') as f:
        points = json.loads(f.read())
    print('Number of distinct points: {0}'.format(len(points)))
    print()

    print('========== 3-letter prefixes ==========')
    prefixes = point_name_prefixes(points, 3)
    for prefix, count in prefixes:
        print(prefix, count)

    print()
    print('========== prefixes up to first . ==========')
    prefixes = point_name_first_components(points)
    for prefix, count in prefixes:
        print(prefix, count)

    print()
    print('========== 2-letter prefixes in point names without "." ==========')
    prefixes = point_names_without_dots_prefixes(points, 3)
    for prefix, count in prefixes:
        print(prefix, count)
