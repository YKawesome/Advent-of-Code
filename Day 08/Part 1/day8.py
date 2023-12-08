

def get_path(lines: list[str]) -> str:
    '''Gets the path description from the lines'''
    return lines[0].strip()


def get_options_dict(lines: list[str]) -> dict[str, dict]:
    '''Gets the options dictionary from the lines'''
    options_dict = {}
    for line in lines:
        line = line.split(' = ')
        curr = line[0]
        remainder = line[1].lstrip('(').rstrip(')').split(', ')
        options_dict[curr] = {
            'L': remainder[0],
            'R': remainder[1]
        }
    return options_dict


def get_file_data(type: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 08/day8{type}.txt')
    return [line.strip() for line in f.readlines()]


def run() -> None:
    '''Runs the program'''
    data = get_file_data('input')
    path = get_path(data)
    del data[0]
    del data[0]
    options_dict = get_options_dict(data)

    curr = 'AAA'

    i = 0
    while curr != 'ZZZ':
        for char in path:
            curr = options_dict[curr][char]
            i += 1
    print(i)


if __name__ == '__main__':
    run()
