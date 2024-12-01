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


def get_seeds(lines: list) -> list[int]:
    '''Returns a list of seeds'''
    seeds = lines[0].strip().split('seeds: ')[1].split(' ')
    seeds = [int(i) for i in seeds]
    del lines[0]
    del lines[0]
    return seeds


def run() -> None:
    '''Runs the program'''
    with open('Day 05/day5input.txt', 'r') as f:
        data = f.read().splitlines()

    seeds = get_seeds(data)
    data = process_data(data)

    seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, \
        light_to_temperature, temperature_to_humidity, humidity_to_location = data

    mappings = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location
    ]

    min_loc = 10_000_000_000
    for seed in seeds:
        for m in mappings:
            for mapping in m:
                if mapping.source_range_start <= seed <= mapping.source_range_start + mapping.range_length:
                    seed = mapping.dest_range_start + (seed - mapping.source_range_start)
                    break
        if seed < min_loc:
            min_loc = seed
    print(min_loc)


if __name__ == '__main__':
    run()
