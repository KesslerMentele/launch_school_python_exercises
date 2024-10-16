"""
Full Description:
The time of day can be represented as the number of minutes before or after
midnight. If the number of minutes is positive, the time is after midnight.
If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns
the time of day in 24-hour format (hh:mm). Your function should work with any
integer input.

You may not use Python's datetime module.


Input: integer
Output: string

Rules:
    Explicit:
        May not use python datetime
        return time in 24-hour format

Algorithm:
    Integer divide by 60, add 24, modulo 24 to get hour
    modulo 60 to get minutes
    return zfilled string coercion in an fstring with a colon

"""


def time_of_day(minutes_from_midnight:int)->str:
    hours = ((minutes_from_midnight // 60) + 24) % 24
    minutes = minutes_from_midnight % 60
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}"



print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
