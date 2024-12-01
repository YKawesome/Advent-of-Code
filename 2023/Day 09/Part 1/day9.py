def get_line_values(line: str) -> list[int]:
    '''Returns the values in the line as a list of ints.'''
    return [int(value) for value in line.split(' ')]


def get_file_data(type: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 09/day9{type}.txt')
    return [line.strip() for line in f.readlines()]


def all_items_zero(data: list[int]) -> bool:
    '''Returns True if all items in the list are 0.'''
    for item in data:
        if item != 0:
            return False
    return True


def sum_last_values(data: list[list[int]]) -> int:
    '''Returns the sum of the last values in each list.'''
    return sum([item[-1] for item in data])


def run() -> None:
    '''Runs the program.'''
    data = [[get_line_values(line)] for line in get_file_data('test')]

    s = 0
    for curr in data:
        for c in curr:
            new = []
            for i in range(1, len(c)):
                new.append(c[i] - c[i - 1])
            curr.append(new)
            if all_items_zero(new):
                break
        s += sum_last_values(curr)

    print(s)



if __name__ == '__main__':
    run()
