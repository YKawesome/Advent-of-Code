def get_file_data(kind: str) -> list[list[str]]:
    '''Gets the data from the file'''
    f = open(f'Day 14/day14{kind}.txt')
    data = [[char for char in line.strip()] for line in f.readlines()]
    f.close()
    return data


def all_os_below_top_or_pound(data: list[list[str]]) -> bool:
    '''Returns whether or not all os below the top are either a top or a pound'''
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O' and data[i - 1][j] not in ['O', '#']:
                return False
    return True


def move_os_up(data: list[list[str]]) -> None:
    '''Moves all os up'''
    for i in range(1, len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O' and data[i - 1][j] not in ['O', '#']:
                data[i - 1][j] = 'O'
                data[i][j] = '.'


def print_data(data: list[list[str]]) -> None:
    '''Prints the data'''
    for line in data:
        for char in line:
            print(char, end='')
        print()


def calculate_load(data: list[list[str]]) -> int:
    '''Calculates the load'''
    load = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'O':
                load += len(data) - i
    return load


def run() -> None:
    '''Runs the program'''
    data = get_file_data('input')
    while not all_os_below_top_or_pound(data):
        move_os_up(data)
    print(calculate_load(data))


if __name__ == '__main__':
    run()
