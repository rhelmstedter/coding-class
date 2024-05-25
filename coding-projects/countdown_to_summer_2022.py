"""A countdown timer until the end of the school year."""
from datetime import datetime
import numpy as np
import time

LAST_DAY_OF_SCHOOL = datetime(2024, 6, 13, 1, 35)
HOLIDAYS_2024 = [
]


def countdown():
    print("\tTime until school is out for summer 2022:", end="\n\n")
    event_delta = LAST_DAY_OF_SCHOOL - datetime.now()
    while (event_delta.days + event_delta.seconds) > 0:
        hours, remaining_delta = divmod(event_delta.seconds, 3600)
        mins, secs = divmod(remaining_delta, 60)
        timer = f"\t{event_delta.days:02d} days {hours:02d} hours {mins:02d} minutes {secs:02d} seconds"
        print(timer, end="\r")
        time.sleep(1)
        event_delta = LAST_DAY_OF_SCHOOL - datetime.now()
    print("School's out for summer!")


def school_days_left():
    today = datetime.now()
    total_minus_weekends = np.busday_count(today.date(), LAST_DAY_OF_SCHOOL.date())
    remaining_holidays = 0
    for holiday in HOLIDAYS_2024:
        if holiday > today.date():
            remaining_holidays += 1
    print()
    print(
        f"\tThere are {total_minus_weekends - remaining_holidays} school days left in the 2021-2022 school year.",
        end="\n\n",
    )


if __name__ == "__main__":
    school_days_left()
    countdown()
