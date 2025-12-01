TEST_INPUT = 'Day 09/day09test.txt'
INPUT = 'Day 09/day09input.txt'


class Block:
    def __init__(self, id: int | str, size: int):
        self._id = id
        self._size = size

    @property
    def id(self):
        return self._id

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    def __str__(self):
        return str(self.id) * self.size

    def __bool__(self):
        return self.id != '.' or self.size == 0


def parse_line(line: str) -> list[Block]:
    blocks = []
    for i in range(len(line)):
        if i % 2 == 0:
            blocks.append(Block(i // 2, int(line[i])))
        else:
            blocks.append(Block('.', int(line[i])))

    return blocks


def get_next_blank(blocks: list[Block], blank: int) -> int:
    while True:
        if blocks[blank]:
            blank += 1
        else:
            break

    return blank


def get_next_end(blocks: list[Block], end: int) -> int:
    while True:
        if blocks[end]:
            end -= 1
        else:
            break

    return end


def compactify(blocks: list[Block]) -> None:
    blank = 0
    end = len(blocks) - 1

    blank = get_next_blank(blocks, blank)
    end = get_next_end(blocks, end)



def main(file) -> None:
    with open(file, 'r') as f:
        line = f.readlines()[0].strip()

    blocks = parse_line(line)
    compactify(blocks)

    for block in blocks:
        print(block, end='')


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    # print(f'Final Output: {main(INPUT)}')
