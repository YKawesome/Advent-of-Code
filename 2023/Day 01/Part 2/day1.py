from collections import namedtuple


_STRINGNUMS = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]
IndexValueTuple = namedtuple('IndexValueTuple', ['index', 'value'])


def get_leftmost_numstring(string: str) -> IndexValueTuple:
    '''Returns the IndexValueTuple of the leftmost "number string", such as "one"'''
    lowest = -1
    value = None
    for num in _STRINGNUMS:
        x = string.find(num[0])
        if x != -1 and (lowest == -1 or x < lowest):
            lowest = x
            value = num[1]
    return IndexValueTuple(lowest, value)


def get_rightmost_numstring(string: str) -> int:
    '''Returns the IndexValueTuple of the rightmost "number string", such as "one"'''
    highest = len(string)
    value = None
    for num in _STRINGNUMS:
        x = string.rfind(num[0])
        if x != -1 and (highest == len(string) or x > highest):
            highest = x
            value = num[1]
    return IndexValueTuple(highest, value)


def get_leftmost_digit(string: str) -> IndexValueTuple:
    '''Returns the IndexValueTuple of the leftmost digit'''
    lowest = -1
    value = None
    for i in range(len(string)):
        if string[i].isdigit():
            lowest = i
            value = int(string[i])
            break
    return IndexValueTuple(lowest, value)


def get_rightmost_digit(string: str) -> IndexValueTuple:
    '''Returns the IndexValueTuple of the rightmost digit'''
    highest = len(string)
    value = None
    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            highest = i
            value = int(string[i])
            break
    return IndexValueTuple(highest, value)


def get_calibration_value(string: str) -> int:
    '''Gets the calibration value from a string'''
    leftmost_numstring = get_leftmost_numstring(string)
    leftmost_digit = get_leftmost_digit(string)
    rightmost_numstring = get_rightmost_numstring(string)
    rightmost_digit = get_rightmost_digit(string)

    if leftmost_numstring.index == -1:
        left = leftmost_digit
    elif leftmost_digit.index == -1:
        left = leftmost_numstring
    else:
        left = leftmost_digit if leftmost_digit.index < leftmost_numstring.index else leftmost_numstring

    if rightmost_numstring.index == len(string):
        right = rightmost_digit
    elif rightmost_digit.index == len(string):
        right = rightmost_numstring
    else:
        right = rightmost_digit if rightmost_digit.index > rightmost_numstring.index else rightmost_numstring

    return left.value * 10 + right.value


def run() -> None:
    '''Runs the program'''
    file = open('Day 01/day1.txt', 'r')
    sum = 0
    for line in file:
        sum += get_calibration_value(line)
    print(sum)


if __name__ == '__main__':
    run()
