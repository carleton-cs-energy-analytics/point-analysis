"""
    value_type_extractor.py
    Alex Davis, January 2019
    Chris Tordi, January 2019

    Script for generating a list of all the enumerations/types from Siemens point description
    reports
"""

import csv
import os
import re

POINT_DESCRIPTION_DIRECTORY = "/Volumes/Seven/Downloads/Siemens Point Descriptions/"


def try_cast_int(s):
    try:
        return int(s)
    except ValueError:
        return None


def try_cast_float(s):
    try:
        return float(s)
    except ValueError:
        return None


def generate_enum_cases_map():
    enum_name_cases_map = {}
    for filename in os.listdir(POINT_DESCRIPTION_DIRECTORY):
        if ".csv" not in filename:
            continue
        print(filename)
        with open(os.path.join(POINT_DESCRIPTION_DIRECTORY, filename), "r") as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                if len(row) == 0 or (len(row) == 1 and len(row[0]) == 0):
                    continue

                if row[0] == "Text Table:":
                    enum_name = row[1]
                    enum_name_cases_map.setdefault(enum_name, set())
                    for caseRow in reader:
                        match = re.match("\s+(\d+)\s+-\s+(\w+)", caseRow[0])
                        if match is None:
                            break

                        enum_name_cases_map[enum_name].add((int(match[1]), match[2]))

    return enum_name_cases_map


def main():
    enum_cases_map = generate_enum_cases_map()
    for enum_name, enum_cases in enum_cases_map.items():
        print(enum_name)
        for case in enum_cases:
            print("\t", case)


if __name__ == "__main__":
    main()
