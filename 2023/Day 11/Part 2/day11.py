from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


def get_file_data(type: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 11/day11{type}.txt')
    return [line.strip() for line in f.readlines()]


def check_line_is_only_periods_or_x(line: str) -> bool:
    '''Returns True if the line is only periods or x'''
    for char in line:
        if char not in ('.', 'x'):
            return False
    return True


def check_line_is_only_x(line: str) -> bool:
    '''Returns True if the line is only x'''
    for char in line:
        if char != 'x':
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


def change_to_x_row(data: list[str], index: int) -> None:
    '''Changes a . row to an x row to the data, at index'''
    data[index] = 'x' * len(data[index])


def change_to_x_col(data: list[str], index: int) -> None:
    '''Changes a . column to an x column to the data, at index'''
    for i in range(len(data)):
        data[i] = data[i][:index] + 'x' + data[i][index + 1:]


def change_x_rows(data: list[str]) -> None:
    '''Changes the period rows to x rows in the data.'''
    for i in range(len(data) - 1, -1, -1):
        row = data[i]
        if check_line_is_only_periods_or_x(row):
            change_to_x_row(data, i)


def change_x_cols(data: list[str]) -> None:
    '''Changes the period columns to x columns in the data.'''
    for i in range(len(data[0]) - 1, -1, -1):
        col = convert_column_to_row(data, i)
        if check_line_is_only_periods_or_x(col):
            change_to_x_col(data, i)


def calculate_distance(p1: Point, p2: Point) -> int:
    '''Calculates the distance between two points.'''
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def run() -> None:
    data = get_file_data('input')

    change_x_rows(data)
    change_x_cols(data)

    galaxies = []
    y_off = 0
    for i in range(len(data)):
        x_off = 0
        for j in range(len(data[i])):
            if check_line_is_only_x(data[i][j:]):
                y_off += 999_999
                break

            if data[i][j] == 'x':
                x_off += 999_999
                continue

            if data[i][j] == '#':
                galaxies.append(Point(j + x_off, i + y_off))

    total = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += calculate_distance(galaxies[i], galaxies[j])

    print(total)


if __name__ == '__main__':
    run()
