TEST_INPUT = "Day 01/day01test.txt"
INPUT = "Day 01/day01input.txt"


def main(file) -> int:
    dial = 50
    count_zeros = 0

    with open(file, "r") as f:
        for line in f:
            sign = 1 if line[0] == "R" else -1
            degrees_to_move = int(line[1:])
            dial_raw = (dial + sign * (degrees_to_move))

            if dial_raw <= 0 and dial > 0:
                count_zeros += 1

            count_zeros += abs(dial_raw) // 100
            # old_dial = dial
            dial = dial_raw % 100

            # print(f"Dial moved from {old_dial} to {dial} using {sign*degrees_to_move} | count_zero={count_zeros}")

    return count_zeros


if __name__ == "__main__":
    print(f"Test Output: {main(TEST_INPUT)}")
    print(f"Final Output: {main(INPUT)}")
