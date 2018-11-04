from decoders.evans_point_decoder import EvansPointDecoder
from decoders.point_decoder import PointDecoder
import json

subClassMap = {'EV': EvansPointDecoder}  # TODO add building mappings as they are discovered and implemented


def get_point_object(name, point):
    prefix = get_prefix(name)
    building_decoder_class = get_building_decoder(prefix)
    building_decoder = building_decoder_class(point)
    return building_decoder.get_point()


def get_building_decoder(prefix):
    return subClassMap.get(prefix, PointDecoder)


def get_prefix(point_name):
    delimiters = {'.', ':', ' ', '-'}
    # calculate index of first delimiter, else None
    first_delimiter_index = next((i for i, ch in enumerate(point_name) if ch in delimiters), None)
    return point_name[:first_delimiter_index] if first_delimiter_index else point_name[:2]


if __name__ == '__main__':
    with open('../data/points.json') as f:
        points = json.loads(f.read())

    point_list = [get_point_object(name, point) for name, point in points.items()]
    print(' Number of points to decode:', len(points))
    print(' Number of points decoded (attempted):', len(point_list))
    print('================ Decoded points (attempted) ================')
    for point in point_list:
        # print(str(point))
        pass
