from itertools import product

TEST_INPUT = 'Day 12/day12test.txt'
INPUT = 'Day 12/day12input.txt'


def extract(file) -> list[list[str]]:
    with open(file, 'r') as f:
        return [[c for c in line.strip()] for line in f.readlines()]


def add_to_p(aps: dict[str, tuple[int, int]], val: str) -> None:
    if val in aps:
        aps[val] = (aps[val][0] + 1, aps[val][1])
    else:
        aps[val] = (1, 0)


def add_to_a(aps: dict[str, tuple[int, int]], val: str) -> None:
    if val in aps:
        aps[val] = (aps[val][0], aps[val][1] + 1)
    else:
        aps[val] = (0, 1)


def add_ap(plot: list[list[str]], aps: dict[str, tuple[int, int]], i: int, j: int) -> None:
    top = i == 0 or plot[i - 1][j] != plot[i][j]
    left = j == 0 or plot[i][j - 1] != plot[i][j]
    bot = i == len(plot) - 1 or plot[i + 1][j] != plot[i][j]
    right = j == len(plot[i]) - 1 or plot[i][j + 1] != plot[i][j]

    dirs = [top, left, bot, right]
    for d in dirs:
        if d:
            add_to_p(aps, plot[i][j])

    add_to_a(aps, plot[i][j])


def main(file) -> None:
    lines = extract(file)
    aps = {}

    for i, j in product(range(len(lines)), range(len(lines[0]))):
        add_ap(lines, aps, i, j)

    return sum([aps[k][0] * aps[k][1] for k in aps.keys()])


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    # print(f'Final Output: {main(INPUT)}')
