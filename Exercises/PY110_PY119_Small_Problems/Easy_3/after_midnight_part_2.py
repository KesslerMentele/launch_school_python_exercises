"""
Full Description:
As seen in the previous exercise, the time of day can be represented as the
number of minutes before or after midnight. If the number of minutes is
positive, the time is after midnight. If the number of minutes is negative,
the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return
the number of minutes before and after midnight, respectively. Both functions
should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Input: String representing 24-hour time
Output: integer representing minutes either before or after midnight

Rules:
    Explicit:
        You may not use pythons datetime module
    Implicit:
        The time is formatted such that:
            time[:2] is the hours
            time[3:] is the minutes

Algorithm:
    coerce time[:2] to int for hours
    coerce time[3:] to int for minutes
    mod 1440 for after time

    coerce time[:2] to int for hours
    coerce time[3:] to int for minutes
    subtract from 1440 the mod 1440 for before time
"""
def after_midnight(time):
    return ((int(time[:2]) * 60) + int(time[3:])) % 1440


def before_midnight(time):
    return (1440 - ((int(time[:2]) * 60) + int(time[3:]))) % 1440


print(after_midnight("00:00") == 0)  # True
print(before_midnight("00:00") == 0)  # True
print(after_midnight("12:34") == 754)  # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)  # True
print(before_midnight("24:00") == 0)  # True