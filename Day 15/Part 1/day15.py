from itertools import product

TEST_INPUT = 'Day 15/day15test.txt'
INPUT = 'Day 15/day15input.txt'

ROBOT = "@"
WALL = "#"
BOX = "O"
SPACE = "."

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

MAPPINGS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}


def extract_lines(file) -> tuple[list[list[str]], tuple[int, int], list[list[str]]]:
    lines = []
    moves = []
    with open(file, 'r') as f:
        while True:
            line = f.readline().strip()
            if line.find(ROBOT) != -1:
                pos = (len(lines), line.find(ROBOT))
            if not line:
                break
            lines.append([c for c in line])

        while line := f.readline().strip():
            moves.extend([c for c in line])

    return lines, pos, moves


def move(lines: list[list[str]], pos: tuple[int, int], direction: str) -> None:
    x, y = pos
    xoff, yoff = MAPPINGS[direction]
    x += xoff
    y += yoff

    if lines[x][y] == WALL:
        return (pos[0], pos[1])
    elif lines[x][y] == BOX:
        if loc := check_box_space(lines, (x, y), direction):
            lines[x][y] = ROBOT
            lines[pos[0]][pos[1]] = SPACE
            lines[loc[0]][loc[1]] = BOX
            return (x, y)
        return (pos[0], pos[1])
    else:
        lines[x][y] = ROBOT
        lines[pos[0]][pos[1]] = SPACE
        return (x, y)


def check_box_space(lines: list[list[str]], pos: tuple[int, int], direction: str) -> tuple[int, int] | None:
    xoff, yoff = MAPPINGS[direction]

    if lines[pos[0] + xoff][pos[1] + yoff] == SPACE:
        return pos[0] + xoff, pos[1] + yoff
    elif lines[pos[0] + xoff][pos[1] + yoff] == BOX:
        return check_box_space(lines, (pos[0] + xoff, pos[1] + yoff), direction)
    else:
        return None


def print_board(lines: list[list[str]]) -> None:
    for line in lines:
        print(''.join(line))


def main(file) -> None:
    lines, pos, moves = extract_lines(file)
    i = 0
    for m in moves:
        pos = move(lines, pos, m)
        i += 1

    total = 0
    for i, j in product(range(len(lines)), range(len(lines[0]))):
        if lines[i][j] == BOX:
            total += 100 * i + j

    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
