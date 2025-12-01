TEST_INPUT = 'Day 01/day01test.txt'
INPUT = 'Day 01/day01input.txt'


def main(file) -> int:
    dial = 50
    count_zeros = 0

    with open(file, 'r') as f:
        for line in f:
            sign = 1 if line[0] == "R" else -1
            degrees_to_move = int(line[1:])
            dial = (dial + sign * (degrees_to_move)) % 100

            if dial == 0:
                count_zeros += 1

    return count_zeros


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
