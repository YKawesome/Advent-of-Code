from collections import OrderedDict


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


def make_hash_table(data: list[str]) -> list[OrderedDict]:
    '''Makes a hash table'''
    boxes: list[OrderedDict] = []
    for _ in range(256):
        boxes.append(OrderedDict())

    for string in data:
        if string[-1] == '-':
            label = string[:-1]
            box = get_hash_number_from_string(label)
            try:
                boxes[box].pop(label)
            except KeyError:
                pass
        else:
            label, val = string.split('=')
            box = get_hash_number_from_string(label)
            boxes[box][label] = int(val)
    return boxes


def calculate_focusing_power_of_box(box: OrderedDict, number: int) -> int:
    '''Calculates the focusing power of a box'''
    total = 0
    for index, val in enumerate(box.values()):
        total += number * (index + 1) * val
    return total


def run() -> None:
    '''Runs the program'''
    data = get_file_data('input')
    boxes = make_hash_table(data)
    total = sum([calculate_focusing_power_of_box(box, index + 1) for index, box in enumerate(boxes)])

    print(total)


if __name__ == '__main__':
    run()
