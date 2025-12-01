TEST_INPUT = 'Day 04/day04test.txt'
INPUT = 'Day 04/day04input.txt'


def extract_lines(file) -> list[str]:
    with open(file, 'r') as f:
        return [line.strip() for line in f.readlines()]


def check_up(lines: list[str], row: int, col: int) -> bool:
    try:
        if row < 3:
            return False
        return lines[row - 1][col] == 'M' and lines[row - 2][col] == 'A' and lines[row - 3][col] == 'S'
    except IndexError:
        return False


def check_down(lines: list[str], row: int, col: int) -> bool:
    try:
        if row > len(lines) - 4:
            return False
        return lines[row + 1][col] == 'M' and lines[row + 2][col] == 'A' and lines[row + 3][col] == 'S'
    except IndexError:
        return False


def check_fwd(lines: list[str], row: int, col: int) -> bool:
    try:
        if col > len(lines[row]) - 4:
            return False
        return lines[row][col + 1] == 'M' and lines[row][col + 2] == 'A' and lines[row][col + 3] == 'S'
    except IndexError:
        return False


def check_bwd(lines: list[str], row: int, col: int) -> bool:
    try:
        if col < 3:
            return False
        return lines[row][col - 1] == 'M' and lines[row][col - 2] == 'A' and lines[row][col - 3] == 'S'
    except IndexError:
        return False


def check_tl_diag(lines: list[str], row: int, col: int) -> bool:
    try:
        if row < 3 or col < 3:
            return False
        return lines[row - 1][col - 1] == 'M' and lines[row - 2][col - 2] == 'A' and lines[row - 3][col - 3] == 'S'
    except IndexError:
        return False


def check_tr_diag(lines: list[str], row: int, col: int) -> bool:
    try:
        if row < 3 or col > len(lines[row]) - 4:
            return False
        return lines[row - 1][col + 1] == 'M' and lines[row - 2][col + 2] == 'A' and lines[row - 3][col + 3] == 'S'
    except IndexError:
        return False


def check_bl_diag(lines: list[str], row: int, col: int) -> bool:
    try:
        if row > len(lines) - 4 or col < 3:
            return False
        return lines[row + 1][col - 1] == 'M' and lines[row + 2][col - 2] == 'A' and lines[row + 3][col - 3] == 'S'
    except IndexError:
        return False


def check_br_diag(lines: list[str], row: int, col: int) -> bool:
    try:
        if row > len(lines) - 4 or col > len(lines[row]) - 4:
            return False
        return lines[row + 1][col + 1] == 'M' and lines[row + 2][col + 2] == 'A' and lines[row + 3][col + 3] == 'S'
    except IndexError:
        return False


def main(file) -> int:
    lines = extract_lines(file)

    xmas = 0

    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'X':
                if check_up(lines, row, col):
                    xmas += 1
                if check_down(lines, row, col):
                    xmas += 1
                if check_fwd(lines, row, col):
                    xmas += 1
                if check_bwd(lines, row, col):
                    xmas += 1
                if check_tl_diag(lines, row, col):
                    xmas += 1
                if check_tr_diag(lines, row, col):
                    xmas += 1
                if check_bl_diag(lines, row, col):
                    xmas += 1
                if check_br_diag(lines, row, col):
                    xmas += 1

    return xmas


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
