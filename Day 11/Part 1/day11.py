TEST_INPUT = 'Day 11/day11test.txt'
INPUT = 'Day 11/day11input.txt'


def extract_stones(file) -> dict[int, int]:
    stones = {}
    with open(file, 'r') as f:
        for stone in f.readlines()[0].strip().split(' '):
            stones[int(stone)] = 1

    return stones


def run_iter(stones: dict[int, int]) -> dict[int, int]:
    newstones = {}
    for stone in stones.keys():
        while stones[stone] > 0:
            if stone == 0:
                if 1 in newstones:
                    newstones[1] += 1
                else:
                    newstones[1] = 1
            elif len(str(stone)) % 2 == 0:
                l = str(stone)[:len(str(stone))//2]
                r = str(stone)[len(str(stone))//2:]
                if int(l) in newstones:
                    newstones[int(l)] += 1
                else:
                    newstones[int(l)] = 1
                if int(r) in newstones:
                    newstones[int(r)] += 1
                else:
                    newstones[int(r)] = 1
            else:
                new = stone * 2024
                if new in newstones:
                    newstones[new] += 1
                else:
                    newstones[new] = 1
            stones[stone] -= 1

    return newstones


def main(file) -> None:
    stones = extract_stones(file)
    ITERS = 25

    for _ in range(ITERS):
        stones = run_iter(stones)

    return sum(stones.values())


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
