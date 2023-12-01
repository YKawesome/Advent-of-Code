def get_calibration_value(string: str) -> int:
    '''Gets the calibration index from a string'''
    left = 0
    for i in range(len(string)):
        if string[i].isdigit():
            left = int(string[i])
            break

    right = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i].isdigit():
            right = int(string[i])
            break 

    return left * 10 + right


def run() -> None:
    '''Runs the program'''
    file = open('Day 01/day1.txt', 'r')
    sum = 0
    for line in file:
        sum += get_calibration_value(line)
    print(sum)


if __name__ == '__main__':
    run()
