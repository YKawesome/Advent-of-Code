def split_line(line: str) -> tuple[list[int], list[int]]:
    '''Splits a winning numbers/your numbers line into two lists of numbers'''
    line = line[0].split(':')[1].strip()
    left, right = line.split(' | ')
    left = [int(i) for i in left.split(' ') if i != '']
    right = [int(i) for i in right.split(' ') if i != '']
    return (left, right)


def get_wins(winning_numbers: list[int], your_numbers: list[int]) -> int:
    '''Returns the number of wins'''
    wins = 0
    for num in your_numbers:
        if num in winning_numbers:
            wins += 1
    return wins


def exponentiate(wins: int) -> None:
    '''Exponentiates the winning numbers'''
    return 2 ** (wins - 1) if wins != 0 else 0


def get_lines() -> list[list[str, int]]:
    '''Returns the lines of the input file'''
    f = open('Day 04/day4input.txt', 'r')
    return [[line.strip(), 1] for line in f]


def add_line_copies(lines: list[str]) -> None:
    '''Adds lines per copy of a card you won'''
    i = 0
    while i < len(lines):
        line = lines[i]
        winning_numbers, your_numbers = split_line(line)
        wins = get_wins(winning_numbers, your_numbers)
        if wins > 0:
            for j in range(wins):
                for _ in range(lines[i][1]):
                    lines[i + j + 1][1] += 1
        i += 1


def run() -> None:
    '''Runs the program'''
    lines = get_lines()
    add_line_copies(lines)
    sum = 0
    for line in lines:
        sum += line[1]
    print(sum)


if __name__ == '__main__':
    run()
