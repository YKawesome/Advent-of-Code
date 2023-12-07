import os
from datetime import datetime
import pytz


def _get_day() -> int:
    '''Returns the current day in EST.'''
    now_utc = datetime.utcnow()
    est_timezone = pytz.timezone('America/New_York')
    now_est = est_timezone.fromutc(now_utc)
    return now_est.day


def run() -> None:
    '''Creates the directories for the current day.'''
    day = str(_get_day())

    os.makedirs(f'Day 0{day}')
    open(f'Day 0{day}/day{day}input.txt', 'w').close()
    open(f'Day 0{day}/day{day}test.txt', 'w').close()

    os.makedirs(f'Day 0{day}/Part 1')
    os.makedirs(f'Day 0{day}/Part 2')

    open(f'Day 0{day}/Part 1/day{day}.py', 'w').close()
    open(f'Day 0{day}/Part 2/day{day}.py', 'w').close()


if __name__ == '__main__':
    run()
