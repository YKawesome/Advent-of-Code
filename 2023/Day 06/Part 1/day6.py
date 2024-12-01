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
    data = [int(i) for i in line if i != ' ' and i != '']
    del lines[0]
    return data


def get_races(lines: list[str]) -> list[Race]:
    '''Gets a list of Races'''
    times = _get_line_data(lines, 'Time')
    distances = _get_line_data(lines, 'Distance')
    races = [Race(times[i], distances[i]) for i in range(len(times))]
    return races


def get_winning_delays(race: Race) -> list[int]:
    '''Returns a list of the winning delays'''
    delays = []
    for i in range(race.time):
        time = race.time - i
        speed = i
        distance = speed * time
        if distance > race.distance:
            delays.append(i)
    return delays


def run() -> None:
    lines = get_lines()
    races = get_races(lines)
    wins_per_race = [len(get_winning_delays(race)) for race in races]
    product = math.prod(wins_per_race)
    print(product)


if __name__ == '__main__':
    run()
