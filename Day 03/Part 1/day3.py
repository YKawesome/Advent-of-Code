from collections import namedtuple

IndexValueLength = namedtuple('IndexValue', ['index', 'value', 'length'])


def symbol_adjacent_to_digit(line_list: list[str], index: tuple[int, int]):
    '''Returns True if any symbol is adjacent to the digit, even diagonally'''
    row = index[0]
    col = index[1]
    t = False
    tr = False
    r = False
    br = False
    b = False
    bl = False
    l = False
    tl = False
    if row > 0:
        t = line_list[row - 1][col] != '.' and not line_list[row - 1][col].isdigit()
        if col > 0:
            tl = line_list[row - 1][col - 1] != '.' and not line_list[row - 1][col - 1].isdigit()
        if col < len(line_list[row]) - 1:
            tr = line_list[row - 1][col + 1] != '.' and not line_list[row - 1][col + 1].isdigit()
    if col > 0:
        l = line_list[row][col - 1] != '.' and not line_list[row][col - 1].isdigit()
    if col < len(line_list[row]) - 1:
        r = line_list[row][col + 1] != '.' and not line_list[row][col + 1].isdigit()
    if row < len(line_list) - 1:
        b = line_list[row + 1][col] != '.' and not line_list[row + 1][col].isdigit()
        if col > 0:
            bl = line_list[row + 1][col - 1] != '.' and not line_list[row + 1][col - 1].isdigit()
        if col < len(line_list[row]) - 1:
            br = line_list[row + 1][col + 1] != '.' and not line_list[row + 1][col + 1].isdigit()

    return t or tr or r or br or b or bl or l or tl


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


def get_lines() -> list[str]:
    '''Returns a list of all the lines in the file'''
    f = open('Day 03/day3.txt', 'r')
    line_list = []
    for line in f:
        line_list.append(line.strip())
    return line_list


def get_nums_list(line_list: list[str]) -> list[int]:
    '''Returns a list of all the numbers in the line list'''
    nums_list = []
    for i in range(len(line_list)):
        line = line_list[i]
        nums = []
        ivls = get_all_numbers_with_starting_index(line)
        for j in range(len(ivls)):
            x = False
            for k in range(ivls[j].length):
                if symbol_adjacent_to_digit(line_list, (i, ivls[j].index + k)):
                    x = True
                if x:
                    value = ivls[j].value
                    # print(value)
                    nums.append(value)
                    break
        nums_list.extend(nums)
    return nums_list


def run() -> None:
    '''Runs the program'''
    line_list = get_lines()
    nums_list = get_nums_list(line_list)
    print(sum(nums_list))


if __name__ == '__main__':
    run()
