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


def get_ranges(mappings_list: list[Mapping], old_ranges: list[range]) -> list[range]:
    '''Returns a list of ranges'''
    ranges = []
    remainders = []

    for ran in old_ranges:
        for mapping in mappings_list:
            offset = mapping.dest_range_start - mapping.source_range_start
            if ran.start >= mapping.source_range_start and ran.stop <= mapping.source_range_start + mapping.range_length:
                ranges.append(range(ran.start + offset, ran.stop + offset))
            elif ran.start < mapping.source_range_start and ran.stop < mapping.source_range_start:
                remainders.append(range(ran.start, ran.stop))
            elif ran.start > mapping.source_range_start + mapping.range_length and ran.stop > mapping.source_range_start + mapping.range_length:
                remainders.append(range(ran.start, ran.stop))
            elif ran.start < mapping.source_range_start and ran.stop > mapping.source_range_start + mapping.range_length:
                ranges.append(range(mapping.source_range_start + offset, mapping.source_range_start + mapping.range_length + offset))
                remainders.append(range(ran.start, mapping.source_range_start))
                remainders.append(range(mapping.source_range_start + mapping.range_length, ran.stop))
            elif ran.start > mapping.source_range_start and ran.stop > mapping.source_range_start + mapping.range_length:
                ranges.append(range(ran.start + offset, mapping.source_range_start + mapping.range_length + offset))
                remainders.append(range(mapping.source_range_start + mapping.range_length, ran.stop))
            elif ran.start < mapping.source_range_start and ran.stop < mapping.source_range_start + mapping.range_length:
                ranges.append(range(mapping.source_range_start + offset, ran.stop + offset))
                remainders.append(range(ran.start, mapping.source_range_start))
    if ranges == []:
        return old_ranges
    return ranges


def run() -> None:
    '''Runs the program'''
    with open('Day 05/day5test.txt', 'r') as f:
        data = f.read().splitlines()

    seeds = get_seeds(data)
    data = process_data(data)

    # seed_to_soil = data[0]

    old_ranges = seeds
    for mappings in data:
        print(old_ranges)
        new_ranges = get_ranges(mappings, old_ranges)
        old_ranges = new_ranges
    # print(old_ranges)


if __name__ == '__main__':
    run()
