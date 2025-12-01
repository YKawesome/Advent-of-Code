from dataclasses import dataclass

TEST_INPUT = 'Day 14/day14test.txt'
INPUT = 'Day 14/day14input.txt'

HEIGHT = 103
WIDTH = 101


@dataclass
class Robot:
    position: tuple[int, int]
    velocity: tuple[int, int]

    def move(self) -> None:
        newx = self.position[0] + self.velocity[0]
        if newx < 0:
            newx += WIDTH
        elif newx >= WIDTH:
            newx -= WIDTH

        newy = self.position[1] + self.velocity[1]
        if newy < 0:
            newy += HEIGHT
        elif newy >= HEIGHT:
            newy -= HEIGHT

        self.position = (newx, newy)


def extract_lines(file) -> list[Robot]:
    robots = []
    with open(file, 'r') as f:
        for line in f:
            pos, vel = line.strip().split(' ')
            pos = pos.lstrip('p=')
            px, py = map(int, pos.split(','))
            vel = vel.lstrip('v=')
            vx, vy = map(int, vel.split(','))

            robots.append(Robot((px, py), (vx, vy)))

    return robots


def main(file) -> None:
    robots = extract_lines(file)
    for _ in range(100):
        for robot in robots:
            robot.move()

    freq = {}
    for robot in robots:
        if robot.position in freq:
            freq[robot.position] += 1
        else:
            freq[robot.position] = 1

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for pos in freq:
        if pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2:
            q1 += freq[pos]
        elif pos[0] >= WIDTH / 2 and pos[1] < HEIGHT // 2:
            q2 += freq[pos]
        elif pos[0] < WIDTH // 2 and pos[1] >= HEIGHT / 2:
            q3 += freq[pos]
        elif pos[0] >= WIDTH / 2 and pos[1] >= HEIGHT / 2:
            q4 += freq[pos]

    return q1 * q2 * q3 * q4


if __name__ == '__main__':
    # print(f'Test Output: {main(TEST_INPUT)}')
    print(f'Final Output: {main(INPUT)}')
