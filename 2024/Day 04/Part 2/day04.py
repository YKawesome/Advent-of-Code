TEST_INPUT = 'Day 04/day04test.txt'
INPUT = 'Day 04/day04input.txt'


def extract_lines(file) -> list[str]:
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def check_x(lines: list[str], row: int, col: int) -> bool:
    if row > len(lines) - 3 or col > len(lines[row]) - 3:
        return False

    l1 = lines[row][col] + lines[row + 1][col + 1] + lines[row + 2][col + 2]
    l2 = lines[row][col + 2] + lines[row + 1][col + 1] + lines[row + 2][col]

    return (l1 == 'MAS' or l1 == 'SAM') and (l2 == 'MAS' or l2 == 'SAM')


def main(file) -> int:
    lines = extract_lines(file)

    xmas = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if check_x(lines, row, col):
                xmas += 1

    return xmas


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
