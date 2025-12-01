from dataclasses import dataclass
from functools import lru_cache


TEST_INPUT = 'Day 13/day13test.txt'
INPUT = 'Day 13/day13input.txt'


@dataclass(frozen=True)
class Machine:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]


def extract_machines(file) -> list[Machine]:
    with open(file, 'r') as f:
        lines = f.readlines()
        return [extract_machine(lines[i:i + 3]) for i in range(0, len(lines), 4)]


def extract_machine(lines: list[str]) -> Machine:
    a = tuple(map(int, lines[0].lstrip("Button A: X+").split(', Y+')))
    b = tuple(map(int, lines[1].lstrip("Button B: X+").split(', Y+')))
    prize = tuple(map(int, lines[2].lstrip("Prize: X=").split(', Y=')))
    return Machine(a, b, prize)


from collections import deque

def solve_machine(machine, tx: int, ty: int) -> int:
    if tx < 0 or ty < 0:
        return -1
    if tx == 0 and ty == 0:
        return 0

    # BFS setup
    queue = deque([(0, 0, 0)])  # (current_tx, current_ty, steps)
    visited = set((0, 0))

    while queue:
        current_tx, current_ty, steps = queue.popleft()

        # Try both moves
        for dx, dy, cost in [(machine.a[0], machine.a[1], 1), (machine.b[0], machine.b[1], 3)]:
            new_tx, new_ty = current_tx + dx, current_ty + dy

            if new_tx == tx and new_ty == ty:
                return steps + cost

            if (new_tx, new_ty) not in visited and new_tx <= tx and new_ty <= ty:
                visited.add((new_tx, new_ty))
                queue.append((new_tx, new_ty, steps + cost))

    return -1


def main(file) -> None:
    machines = extract_machines(file)
    total = 0
    for machine in machines:
        s = solve_machine(machine, *machine.prize)
        if s != -1:
            total += s
            print(s)
    
    return total


if __name__ == '__main__':
    print(f'Test Output: {main(TEST_INPUT)}')
    # print(f'Final Output: {main(INPUT)}')
