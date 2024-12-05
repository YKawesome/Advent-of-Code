import os
from datetime import datetime, timezone
import pytz


def _get_day() -> int:
    '''Returns the current day in EST.'''
    now_utc = datetime.now(timezone.utc)  # Timezone-aware UTC datetime
    est_timezone = pytz.timezone('America/New_York')
    now_est = now_utc.astimezone(est_timezone)  # Convert directly to EST
    return now_est.day


def run(day=None) -> None:
    '''Creates the directories for the current day and writes the required lines to Python files.'''
    if not day:
        day = str(_get_day())
        day = day if len(day) == 2 else '0' + day

    # Create directories and files
    os.makedirs(f'Day {day}', exist_ok=True)
    open(f'Day {day}/day{day}input.txt', 'w').close()
    open(f'Day {day}/day{day}test.txt', 'w').close()

    os.makedirs(f'Day {day}/Part 1', exist_ok=True)
    os.makedirs(f'Day {day}/Part 2', exist_ok=True)

    part1_file = f'Day {day}/Part 1/day{day}.py'
    part2_file = f'Day {day}/Part 2/day{day}.py'

    # Write to both Python files
    content = f"""TEST_INPUT = 'Day {day}/day{day}test.txt'
INPUT = 'Day {day}/day{day}input.txt'


def main(file) -> None:
    pass


if __name__ == '__main__':
    print(f'Test Output: {{main(TEST_INPUT)}}')
    print(f'Final Output: {{main(INPUT)}}')
"""

    with open(part1_file, 'w') as f1:
        f1.write(content)

    with open(part2_file, 'w') as f2:
        f2.write(content)


if __name__ == '__main__':
    d = input('Enter the day number [blank for auto]: ')
    if d == '':
        run()
    else:
        run(d)
