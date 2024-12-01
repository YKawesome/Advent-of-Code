from collections import namedtuple

IndexValueLength = namedtuple('IndexValue', ['index', 'value', 'length'])


def get_all_numbers_with_starting_index(line: str) -> list[IndexValueLength]:
    '''Returns all numbers in a line with their starting index'''
    numsstr = ''
    first_non_num = False
    index = None
    index_str = ''
    length = 0
    length_str = ''
    for i in range(len(line)):
        if line[i].isdigit():
            numsstr += line[i]
            first_non_num = False
            if index is None:
                index = i
                index_str += str(index) + ' '
            length += 1
            if i == len(line) - 1:
                length_str += str(length) + ' '
        else:
            if not first_non_num:
                first_non_num = True
                numsstr += ' '
                index = None
                if length != 0:
                    length_str += str(length) + ' '
                length = 0
            else:
                continue
    numsstr = numsstr.strip()
    index_str = index_str.strip()
    length_str = length_str.strip()
    nums = numsstr.split(' ')
    indexes = index_str.split(' ')
    lengths = length_str.split(' ')
    try:
        index_values = [IndexValueLength(int(index), int(value), int(length)) for (index, value, length) in zip(indexes, nums, lengths)]
        return index_values
    except ValueError:
        return []


def check_length_three(line_list: list[str], row: int, ivl: IndexValueLength) -> list[tuple[tuple[int, int], int]]:
    '''Returns the location of all * that are adjacent to a number of length 3 in line_list'''
    ret_list = []
    col = ivl.index
    if row > 0:
        if col > 0:
            if line_list[row - 1][col - 1] == '*':
                ret_list.append(((row - 1, col - 1), ivl.value))  # Topleftleft
        if line_list[row - 1][col] == '*':
            ret_list.append(((row - 1, col), ivl.value))  # Topleft
        if line_list[row - 1][col + 1] == '*':
            ret_list.append(((row - 1, col + 1), ivl.value))  # Top
        if line_list[row - 1][col + 2] == '*':
            ret_list.append(((row - 1, col + 2), ivl.value))  # Topright
        if col + 3 < len(line_list[row]):
            if line_list[row - 1][col + 3] == '*':
                ret_list.append(((row - 1, col + 3), ivl.value))  # Toprightright
    if col > 0:
        if line_list[row][col - 1] == '*':
            ret_list.append(((row, col - 1), ivl.value))  # Left
    if col + 3 < len(line_list[row]):
        if line_list[row][col + 3] == '*':
            ret_list.append(((row, col + 3), ivl.value))  # Right
    if row < len(line_list) - 1:
        if col > 0:
            if line_list[row + 1][col - 1] == '*':
                ret_list.append(((row + 1, col - 1), ivl.value))  # Bottomleftleft
        if line_list[row + 1][col] == '*':
            ret_list.append(((row + 1, col), ivl.value))  # Bottomleft
        if line_list[row + 1][col + 1] == '*':
            ret_list.append(((row + 1, col + 1), ivl.value))  # Bottom
        if line_list[row + 1][col + 2] == '*':
            ret_list.append(((row + 1, col + 2), ivl.value))  # Bottomright
        if col + 3 < len(line_list[row]):
            if line_list[row + 1][col + 3] == '*':
                ret_list.append(((row + 1, col + 3), ivl.value))  # Bottomrightright
    return ret_list


def check_length_two(line_list: list[str], row: int, ivl: IndexValueLength) -> list[tuple[tuple[int, int], int]]:
    '''Returns the location of all * that are adjacent to a number of length 2 in line_list'''
    ret_list = []
    col = ivl.index
    if row > 0:
        if col > 0:
            if line_list[row - 1][col - 1] == '*':
                ret_list.append(((row - 1, col - 1), ivl.value))  # Topleft
        if line_list[row - 1][col] == '*':
            ret_list.append(((row - 1, col), ivl.value))  # Top1
        if line_list[row - 1][col + 1] == '*':
            ret_list.append(((row - 1, col + 1), ivl.value))  # Top2
        if col + 2 < len(line_list[row]):
            if line_list[row - 1][col + 2] == '*':
                ret_list.append(((row - 1, col + 2), ivl.value))  # Topright
    if col > 0:
        if line_list[row][col - 1] == '*':
            ret_list.append(((row, col - 1), ivl.value))  # Left
    if col + 2 < len(line_list[row]):
        if line_list[row][col + 2] == '*':
            ret_list.append(((row, col + 2), ivl.value))  # Right
    if row < len(line_list) - 1:
        if col > 0:
            if line_list[row + 1][col - 1] == '*':
                ret_list.append(((row + 1, col - 1), ivl.value))  # Bottomleft
        if line_list[row + 1][col] == '*':
            ret_list.append(((row + 1, col), ivl.value))  # Bottom1
        if line_list[row + 1][col + 1] == '*':
            ret_list.append(((row + 1, col + 1), ivl.value))  # Bottom2
        if col + 2 < len(line_list[row]):
            if line_list[row + 1][col + 2] == '*':
                ret_list.append(((row + 1, col + 2), ivl.value)) # Bottomright
    return ret_list


def check_length_one(line_list: list[str], row: int, ivl: IndexValueLength) -> list[tuple[tuple[int, int], int]]:
    '''Returns the location of all * that are adjacent to a number of length 1 in line_list'''
    ret_list = []
    col = ivl.index
    if row > 0:
        if col > 0:
            if line_list[row - 1][col - 1] == '*':
                ret_list.append(((row - 1, col - 1), ivl.value))  # Topleft
        if line_list[row - 1][col] == '*':
            ret_list.append(((row - 1, col), ivl.value))  # Top
        if col + 1 < len(line_list[row]):
            if line_list[row - 1][col + 1] == '*':
                ret_list.append(((row - 1, col + 1), ivl.value))  # Topright
    if col > 0:
        if line_list[row][col - 1] == '*':
            ret_list.append(((row, col - 1), ivl.value))  # Left
    if col + 1 < len(line_list[row]):
        if line_list[row][col + 1] == '*':
            ret_list.append(((row, col + 1), ivl.value))  # Right
    if row < len(line_list) - 1:
        if col > 0:
            if line_list[row + 1][col - 1] == '*':
                ret_list.append(((row + 1, col - 1), ivl.value))  # Bottomleft
        if line_list[row + 1][col] == '*':
            ret_list.append(((row + 1, col), ivl.value))  # Bottom
        if col + 1 < len(line_list[row]):
            if line_list[row + 1][col + 1] == '*':
                ret_list.append(((row + 1, col + 1), ivl.value))  # Bottomright
    return ret_list


def get_line_list() -> list[str]:
    '''Returns a list of lines from the input file'''
    f = open('Day 03/day3.txt', 'r')
    line_list = []
    for line in f:
        line_list.append(line.strip())
    return line_list


def get_numdict(line_list: list[str]) -> dict[tuple, list[int]]:
    '''Returns a dictionary of locations of stars and the associated numbers'''
    numdict = dict()
    for i in range(len(line_list)):
        line = line_list[i]
        ivls = get_all_numbers_with_starting_index(line)
        for ivl in ivls:
            if ivl.length == 3:
                x = check_length_three(line_list, i, ivl)
            elif ivl.length == 2:
                x = check_length_two(line_list, i, ivl)
            elif ivl.length == 1:
                x = check_length_one(line_list, i, ivl)
            else:
                continue
            for tup in x:
                if tup[0] not in numdict:
                    numdict[tup[0]] = [tup[1]]
                else:
                    numdict[tup[0]].append(tup[1])
    return numdict


def get_sum_of_products(numdict: dict[tuple, list[int]]) -> int:
    '''Returns the sum of all products in numdict'''
    sum = 0
    for item in numdict.items():
        if len(item[1]) > 1:
            prod = 1
            for num in item[1]:
                prod *= num
            sum += prod
    return sum


def run() -> None:
    '''Runs the program'''
    line_list = get_line_list()
    numdict = get_numdict(line_list)
    sum = get_sum_of_products(numdict)
    print(sum)


if __name__ == '__main__':
    run()
