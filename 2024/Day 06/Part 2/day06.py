TEST_INPUT = 'Day 06/day06test.txt'
INPUT = 'Day 06/day06input.txt'

UNSEEN = 0
SEEN = 1
OBSTACLE = 2

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


def extract_lines(file) -> tuple[tuple[int, int], list[list[int]]]:
    with open(file, 'r') as f:
        lines = [[c for c in line.strip()] for line in f.readlines()]

    guard = None
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '^':
                lines[i][j] = SEEN
                guard = (i, j)
            elif lines[i][j] == '#' or lines[i][j] == 'O':
                lines[i][j] = OBSTACLE
            else:
                lines[i][j] = UNSEEN

    return guard, lines


def check_iter(guard: tuple[int, int], lines: list[list[int]], direction: int) -> int:
    seen = set()
    while 0 <= guard[0] < len(lines) and 0 <= guard[1] < len(lines[0]):
        if (guard[0], guard[1], direction) in seen:
            return 1

        x, y = guard
        seen.add((x, y, direction))

        ahead = (guard[0] - 1, guard[1]) if direction == UP else \
            (guard[0], guard[1] + 1) if direction == RIGHT else \
            (guard[0] + 1, guard[1]) if direction == DOWN else \
            (guard[0], guard[1] - 1)

        try:
            if lines[ahead[0]][ahead[1]] == OBSTACLE:
                direction = (direction + 1) % 4
                continue
        except IndexError:
            break

        guard = ahead

    return 0


def main(file) -> int:
    guard, lines = extract_lines(file)
    direction = UP

    tot = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == UNSEEN:
                newlines = [line.copy() for line in lines]
                newlines[i][j] = OBSTACLE
                tot += check_iter(guard, newlines, direction)

    return tot


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
