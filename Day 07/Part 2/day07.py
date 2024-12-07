from collections import deque

TEST_INPUT = 'Day 07/day07test.txt'
INPUT = 'Day 07/day07input.txt'


def extract_lines(file) -> list[str]:
    with open(file, 'r') as f:
        return [line.strip() for line in f.read().splitlines()]


def format_lines(lines: list[str]) -> list[tuple[int, deque[int]]]:
    return [(int(line.split()[0][:-1]), deque(int(x) for x in line.split()[1:])) for line in lines]


def check_line(target, nums, total) -> bool:
    if total == target and not nums:
        return True

    if total > target:
        return False

    if not nums:
        return False

    num = nums.popleft()
    try_add = check_line(target, nums.copy(), total + num)
    try_mult = check_line(target, nums.copy(), total * num if total != 0 else num)
    try_concat = check_line(target, nums.copy(), int(str(total) + str(num)))
    return try_add or try_mult or try_concat


def main(file) -> int:
    lines = format_lines(extract_lines(file))
    valid = 0
    for line in lines:
        check = check_line(line[0], line[1].copy(), 0)
        if check:
            valid += line[0]

    return valid


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
    # print(check_line(7290, deque([6, 8, 6, 15]), 0))
