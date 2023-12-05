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
    # s = set()
    # for r in ranges:
    #     print(r)
    #     s.update(r)
    # seeds = []

    # for i in s:
    #     print(i)

    del lines[0]
    del lines[0]
    return ranges


def run() -> None:
    '''Runs the program'''
    with open('Day 05/day5input.txt', 'r') as f:
        data = f.read().splitlines()

    seeds = get_seeds(data)
    data = process_data(data)

    # seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, \
    #     light_to_temperature, temperature_to_humidity, humidity_to_location = data

    # mappings = [
    #     seed_to_soil,
    #     soil_to_fertilizer,
    #     fertilizer_to_water,
    #     water_to_light,
    #     light_to_temperature,
    #     temperature_to_humidity,
    #     humidity_to_location
    # ]
    # print(seeds)
    # print(data)
    data.reverse()
    # print(data)
    # print(min(map(lambda x: map_seed_to_location(x, mappings), seeds)))
    min = 10_000_000_000
    print('starting up')
    for seed_range in seeds:
        i = 0
        print(seed_range)
        while True:
            if seed_range.start <= map_location_to_seed(i, data) < seed_range.stop:
                if i < min:
                    min = i
                break
            i += 1
            if i % 100_000 == 0:
                print(i)
    print(min)


def map_location_to_seed(location: int, mappings: list[list[Mapping]]) -> int:
    '''Maps a location to a seed'''
    for m in mappings:
        for mapping in m:
            if mapping.dest_range_start <= location <= mapping.dest_range_start + mapping.range_length:
                location -= mapping.dest_range_start - mapping.source_range_start
                break
    return location


if __name__ == '__main__':
    run()
