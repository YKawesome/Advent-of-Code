import re

TEST_INPUT = 'Day 03/day03test.txt'
INPUT = 'Day 03/day03input.txt'


def extract_lines(file) -> list[str]:
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main(file) -> int:
    lines = extract_lines(file)
    total = 0

    for line in lines:
        words = re.findall(r'mul\(\d+,\d+\)', line)
        words = [[int(x) for x in w[4:-1].split(',')] for w in words]
        total += sum([x * y for x, y in words])

    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
