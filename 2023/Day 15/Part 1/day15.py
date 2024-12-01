def get_file_data(kind: str) -> list[str]:
    '''Gets the data from the file'''
    f = open(f'Day 15/day15{kind}.txt', 'r')
    return f.readlines()[0].strip().split(',')


def mutate_number(number: int, char: str) -> int:
    '''Mutates a number with the HASH algorithm'''
    return ((number + ord(char)) * 17) % 256


def get_hash_number_from_string(string: str) -> int:
    '''Gets the HASH value from a string'''
    number = 0
    for char in string:
        number = mutate_number(number, char)
    return number


def run() -> None:
    '''Runs the program'''
    data = get_file_data('input')
    total = sum([get_hash_number_from_string(string) for string in data])
    print(total)


if __name__ == '__main__':
    run()
