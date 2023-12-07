# THIS CODE DOES NOT WORK

from collections import namedtuple


Mapping = namedtuple('Mapping', ['dest_range_start', 'source_range_start', 'range_length'])


def process_data(lines: list) -> list[list[Mapping]]:
    '''Returns a list of lists of mapping data'''
    data = []
    curr_list_index = -1

    for i in range(len(lines)):
        if lines[i].strip() == '':
            continue
        else:
            if not lines[i].strip()[0].isdigit():
                data.append([])
                curr_list_index += 1
            else:
                app = [int(i) for i in lines[i].split()]
                mapping = Mapping(app[0], app[1], app[2])
                data[curr_list_index].append(mapping)
    return data


def get_seeds(lines: list) -> list[range]:
    '''Returns a list of seeds'''
    line = lines[0].strip().split('seeds: ')[1].split(' ')
    i = 0
    ranges = []
    while i < len(line):
        if i % 2 == 0:
            ranges.append([int(line[i]), int(line[i + 1])])
        i += 1

    ranges = [range(i[0], i[0] + i[1]) for i in ranges]

    del lines[0]
    del lines[0]
    return ranges


def map_location_to_seed(location: int, mappings: list[list[Mapping]]) -> int:
    '''Maps a location to a seed'''
    for m in reversed(mappings):
        for mapping in m:
            if mapping.dest_range_start <= location <= mapping.dest_range_start + mapping.range_length:
                location -= mapping.dest_range_start - mapping.source_range_start
                break
    return location


def check_valid_location(location: int, seedranges: list[range], mappings: list[list[Mapping]]) -> bool:
    '''Checks if a location is valid'''
    for r in seedranges:
        if map_location_to_seed(location, mappings) in r:
            return True
    return False


def run() -> None:
    '''Runs the program'''
    with open('Day 05/day5input.txt', 'r') as f:
        data = f.read().splitlines()

    seeds = get_seeds(data)
    data = process_data(data)

    low = 0
    high = 1_000_000_00
    while low < high:
        mid = (low + high) // 2
        if check_valid_location(mid, seeds, data):
            high = mid
        else:
            low = mid + 1
    print(mid)



if __name__ == '__main__':
    run()
