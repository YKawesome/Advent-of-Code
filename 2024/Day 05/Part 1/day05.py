TEST_INPUT = 'Day 05/day05test.txt'
INPUT = 'Day 05/day05input.txt'


def extract_lines(file):
    with open(file, 'r') as f:
        lines = (line.strip() for line in f.readlines())
    for line in lines:
        if line == '':
            yield None
            break
        else:
            yield tuple(int(x) for x in line.split('|'))

    for line in lines:
        yield [int(x) for x in line.split(',')]


def check_seq(sequence: list[int], beforedict: dict[int, set[int]]) -> bool:
    past = set()
    for i in sequence:
        if i in past:
            return False
        if i in beforedict:
            past = past.union(beforedict[i])

    return True


def main(file) -> None:
    lines = extract_lines(file)
    beforedict: dict[int, set[int]] = {}

    for line in lines:
        if line is None:
            break
        a, b = line

        if b not in beforedict:
            beforedict[b] = set()

        beforedict[b].add(a)

    tot = 0
    for sequence in lines:
        if check_seq(sequence, beforedict):
            tot += sequence[len(sequence) // 2]

    return tot


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
