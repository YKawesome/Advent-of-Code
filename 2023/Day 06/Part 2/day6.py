from collections import namedtuple
import math

Race = namedtuple('Race', ['time', 'distance'])


def get_lines() -> list[str]:
    '''Returns a list of lines'''
    f = open('Day 06/day6input.txt', 'r')
    lines = f.read().splitlines()
    return lines


def _get_line_data(lines: list, first: str) -> list[int]:
    '''Returns a list of times'''
    line = lines[0].strip().split(f'{first}: ')[1].split(' ')
    data = [i for i in line if i != ' ' and i != '']
    data = [int(''.join(data))]
    del lines[0]
    return data


def get_races(lines: list[str]) -> list[Race]:
    '''Gets a list of Races'''
    times = _get_line_data(lines, 'Time')
    distances = _get_line_data(lines, 'Distance')
    races = [Race(times[i], distances[i]) for i in range(len(times))]
    return races


def get_winning_delays_count(race: Race) -> int:
    '''Returns a count of the winning delays'''
    a = -1
    b = race.time
    c = -1 * race.distance

    center = -b / (2 * a)
    offset = math.sqrt(b ** 2 - 4 * a * c) / (2 * a)

    x1 = center + offset
    x2 = center - offset

    diff = math.ceil(x2) - math.floor(x1) - 1

    return diff


def run() -> None:
    lines = get_lines()
    races = get_races(lines)
    print(get_winning_delays_count(races[0]))


if __name__ == '__main__':
    run()
