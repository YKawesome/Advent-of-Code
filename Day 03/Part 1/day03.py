import re

TEST_INPUT = 'Day 03/day03test.txt'
INPUT = 'Day 03/day03input.txt'


def extract_lines(file) -> list[str]:
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def main(file) -> int:
    lines = extract_lines(file)
    line = ''.join(lines)
    total = 0

    words = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for i in range(len(words)):
        if 'mul' in words[i]:
            a, b = map(int, re.findall(r"\d+", words[i]))
            words[i] = a * b

    print(words)
    do = True
    for item in words:
        if item == 'do()':
            do = True
        elif item == "don't()":
            do = False
        elif do:
            total += item

    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
