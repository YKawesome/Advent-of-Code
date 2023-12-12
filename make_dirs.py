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
    day = day if len(day) == 2 else '0' + day

    os.makedirs(f'Day {day}')
    open(f'Day {day}/day{day}input.txt', 'w').close()
    open(f'Day {day}/day{day}test.txt', 'w').close()

    os.makedirs(f'Day {day}/Part 1')
    os.makedirs(f'Day {day}/Part 2')

    open(f'Day {day}/Part 1/day{day}.py', 'w').close()
    open(f'Day {day}/Part 2/day{day}.py', 'w').close()


if __name__ == '__main__':
    run()
