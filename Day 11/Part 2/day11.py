TEST_INPUT = 'Day 11/day11test.txt'
INPUT = 'Day 11/day11input.txt'


def extract_stones(file) -> dict[int, int]:
    stones = {}
    with open(file, 'r') as f:
        for stone in f.readlines()[0].strip().split(' '):
            stones[int(stone)] = 1

    return stones


def handle_0(count: int, newstones: dict[int, int]):
    if 1 in newstones:
        newstones[1] += count
    else:
        newstones[1] = count


def handle_even(stone: int, count: int, newstones: dict[int, int]):
    l = str(stone)[:len(str(stone))//2]
    r = str(stone)[len(str(stone))//2:]
    if int(l) in newstones:
        newstones[int(l)] += count
    else:
        newstones[int(l)] = count
    if int(r) in newstones:
        newstones[int(r)] += count
    else:
        newstones[int(r)] = count


def handle_else(stone: int, count: int, newstones: dict[int, int]):
    new = stone * 2024
    if new in newstones:
        newstones[new] += count
    else:
        newstones[new] = count


def run_iter(stones: dict[int, int]) -> dict[int, int]:
    newstones = {}
    for stone in stones.keys():
        if stone == 0:
            handle_0(stones[stone], newstones)
        elif len(str(stone)) % 2 == 0:
            handle_even(stone, stones[stone], newstones)
        else:
            handle_else(stone, stones[stone], newstones)

    return newstones


def main(file) -> None:
    stones = extract_stones(file)
    ITERS = 75

    for i in range(ITERS):
        stones = run_iter(stones)

    return sum(stones.values())


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
