#!/usr/bin/env python3
'''
    Jeff's quick dump of the Siemens point definitions into a
    JSON string. If we want the JSON structured differently,
    it's easy to whack at this script to make it happen.
'''

import sys
import os
import csv
import json

# The structure to print out as JSON
points = {}

# Tracking the contents of the current point
current_point = {}
current_point_name = ''

# Statistics for report
key_counts = {}

# For each CSV file
for file_name in os.listdir('.'):
    if file_name[-4:] != '.csv':
        continue

    # Process the file
    with open(file_name) as f:
        line_number = 0
        reader = csv.reader(f)
        for row in reader:
            line_number += 1
            # Empty row 
            if len(row) == 0 or (len(row) == 1 and len(row[0]) == 0):
                continue

            # End-of-point marker
            if len(row) > 0 and '******' in row[0]:
                if current_point_name:
                    if current_point_name in points:
                        print('[{0}:{1}] Duplicate point name: {2}'.format(file_name, line_number, current_point_name), file=sys.stderr)
                    else:
                        points[current_point_name] = current_point

                current_point = {}
                current_point_name = ''
                continue

            # Record key/value pairs
            if row[0][-1] == ':':
                key = row[0][:-1]
                key_counts[key] = key_counts.get(key, 0) + 1
                value = row[1:]
                current_point[key] = row[1:]
                if key == 'Point Name':
                    if current_point_name:
                        print('[{0}:{1}] Second Point Name in one point:'.format(file_name, line_number), file=sys.stderr)
                    current_point_name = row[1]

# Save the points as JSON
with open('points.json', 'w') as f:
    f.write(json.dumps(points))

# Print the report to stderr
for key in sorted(key_counts, key=key_counts.get, reverse=True):
    print(key, key_counts[key])
print('point count:', len(points), file=sys.stderr)
