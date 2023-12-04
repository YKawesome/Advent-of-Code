def split_line(line: str) -> tuple[list[int], list[int]]:
    '''Splits a winning numbers/your numbers line into two lists of numbers'''
    line = line.split(':')[1].strip()
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


def run() -> None:
    '''Runs the program'''
    f = open('Day 04/day4input.txt', 'r')
    sum = 0
    for line in f:
        winning_numbers, your_numbers = split_line(line)
        wins = get_wins(winning_numbers, your_numbers)
        sum += exponentiate(wins)
    print(sum)


if __name__ == '__main__':
    run()
