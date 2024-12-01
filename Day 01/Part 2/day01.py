TEST_INPUT = 'Day 01/day01test.txt'
INPUT = 'Day 01/day01input.txt'


def extract_lines(file) -> tuple[list[str]]:
    l1 = []
    l2 = []

    with open(file, 'r') as f:
        for line in f:
            l1.append(line.split('   ')[0].strip())
            l2.append(line.split('   ')[1].strip())

    return l1, l2


def main(file) -> str:
    l1, l2 = extract_lines(file)

    total = 0
    for n in l1:
        total += int(n) * l2.count(n)

    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
