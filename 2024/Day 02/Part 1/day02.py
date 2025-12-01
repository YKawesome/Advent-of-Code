TEST_INPUT = 'Day 02/day02test.txt'
INPUT = 'Day 02/day02input.txt'


def extract_lines(file) -> list[list[int]]:
    with open(file, 'r') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]

    return [[int(i) for i in line] for line in lines]


def check_valid(line: list[int]) -> bool:
    inc = check_inc(line)
    dec = check_dec(line)
    adj = check_adj(line)

    if (isinstance(inc, bool) and inc or isinstance(dec, bool) and dec) and isinstance(adj, bool) and adj:
        return True
    elif isinstance(adj, int):
        line.pop(adj)
        inc = check_inc(line)
        dec = check_dec(line)
        adj = check_adj(line)

        if (isinstance(inc, bool) and inc or isinstance(dec, bool) and dec) and isinstance(adj, bool) and adj:
            return True
    elif isinstance(inc, int):
        line.pop(inc)
        inc = check_inc(line)
        dec = check_dec(line)
        adj = check_adj(line)

        if (isinstance(inc, bool) and inc or isinstance(dec, bool) and dec) and isinstance(adj, bool) and adj:
            return True
    elif isinstance(dec, int):
        line.pop(dec)
        inc = check_inc(line)
        dec = check_dec(line)
        adj = check_adj(line)

        if (isinstance(inc, bool) and inc or isinstance(dec, bool) and dec) and isinstance(adj, bool) and adj:
            return True

    return False


def check_inc(line: list[int]) -> bool | int:
    prev = None
    for idx, i in enumerate(line):
        if prev is None:
            prev = i
            continue

        if i < prev:
            return idx

        prev = i

    return True


def check_dec(line: list[int]) -> bool | int:
    prev = None
    for idx, i in enumerate(line):
        if prev is None:
            prev = i
            continue

        if i > prev:
            return idx

        prev = i

    return True


def check_adj(line: list[int]) -> bool | int:
    prev = None
    for idx, i in enumerate(line):
        if prev is None:
            prev = i
            continue

        if not (1 <= abs(i - prev) <= 3):
            return idx

        prev = i

    return True


def main(file) -> int:
    lines = extract_lines(file)
    total = 0

    for line in lines:
        if check_valid(line):
            total += 1

    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
