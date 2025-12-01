TEST_INPUT = 'Day 08/day08test.txt'
INPUT = 'Day 08/day08input.txt'


class Node:
    def __init__(self, antenna: str = None):
        self._anti = False
        self._antenna = antenna

    @property
    def anti(self):
        return self._anti

    @anti.setter
    def anti(self, value: bool):
        self._anti = value

    @property
    def antenna(self):
        return self._antenna

    def __bool__(self):
        return self.anti

    def __eq__(self, other):
        return self.antenna == other.antenna


def extract_lines(file) -> list[list[Node]]:
    



def main(file) -> None:
    pass


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
