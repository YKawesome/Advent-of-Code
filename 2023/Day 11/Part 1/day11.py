from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def get_file_data(type: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 11/day11{type}.txt')
    return [line.strip() for line in f.readlines()]


def check_line_is_only_periods(line: str) -> bool:
    '''Returns True if the line is only periods.'''
    for char in line:
        if char != '.':
            return False
    return True


def convert_column_to_row(data: list[str], index: int) -> str:
    '''Converts the column to a row.'''
    new = ''
    try:
        for i in range(len(data[index])):
            new += data[i][index]
    except IndexError:
        return new
    return new


def add_period_row(data: list[str], index: int) -> None:
    '''Adds a period row to the data, before index'''
    data.insert(index, '.' * len(data[0]))


def add_period_col(data: list[str], index: int) -> None:
    '''Adds a period column to the data, before index'''
    for i in range(len(data)):
        data[i] = data[i][:index] + '.' + data[i][index:]


def double_period_rows(data: list[str]) -> None:
    '''Doubles the period rows in the data.'''
    for i in range(len(data) - 1, -1, -1):
        row = data[i]
        if check_line_is_only_periods(row):
            add_period_row(data, i)


def double_period_cols(data: list[str]) -> None:
    '''Doubles the period columns in the data.'''
    for i in range(len(data[0]) - 1, -1, -1):
        col = convert_column_to_row(data, i)
        if check_line_is_only_periods(col):
            add_period_col(data, i)


def calculate_distance(p1: Point, p2: Point) -> int:
    '''Calculates the distance between two points.'''
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def run() -> None:
    data = get_file_data('input')
    double_period_rows(data)
    double_period_cols(data)

    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                galaxies.append(Point(j, i))

    total = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += calculate_distance(galaxies[i], galaxies[j])

    print(total)


if __name__ == '__main__':
    run()
