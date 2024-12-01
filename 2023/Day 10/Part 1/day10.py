from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

_UP = 0
_RIGHT = 1
_DOWN = 2
_LEFT = 3


def get_file_data(type: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 10/day10{type}.txt')
    return [[char for char in line.strip()] for line in f.readlines()]


def find_starting_position(data: list[str]) -> Point:
    '''Finds the starting position.'''
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                return Point(x, y)


def transform_point(point: Point, char: str, dir: int) -> tuple[Point, int]:
    '''Transfomrs a Point using the char transformation.'''
    if char == '|':
        if dir == _UP:
            return Point(point.x, point.y - 1), dir
        elif dir == _DOWN:
            return Point(point.x, point.y + 1), dir
    elif char == '-':
        if dir == _RIGHT:
            return Point(point.x + 1, point.y), dir
        elif dir == _LEFT:
            return Point(point.x - 1, point.y), dir
    elif char == 'L':
        if dir == _LEFT:
            return Point(point.x, point.y - 1), _UP
        elif dir == _DOWN:
            return Point(point.x + 1, point.y), _RIGHT
    elif char == 'J':
        if dir == _DOWN:
            return Point(point.x - 1, point.y), _LEFT
        elif dir == _RIGHT:
            return Point(point.x, point.y - 1), _UP
    elif char == '7':
        if dir == _UP:
            return Point(point.x - 1, point.y), _LEFT
        elif dir == _RIGHT:
            return Point(point.x, point.y + 1), _DOWN
    elif char == 'F':
        if dir == _UP:
            return Point(point.x + 1, point.y), _RIGHT
        elif dir == _LEFT:
            return Point(point.x, point.y + 1), _DOWN
    elif char == 'S':
        return point, -1


def run() -> None:
    '''Runs the program.'''
    data = get_file_data('input')

    point = find_starting_position(data)
    s_dir = _LEFT
    point, s_dir = transform_point(point, 'F', s_dir)

    count = 1
    while True:
        point, s_dir = transform_point(point, data[point.y][point.x], s_dir)
        if s_dir == -1:
            break
        count += 1

    print(count // 2)


if __name__ == '__main__':
    run()