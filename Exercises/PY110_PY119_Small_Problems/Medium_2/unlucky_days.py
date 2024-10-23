"""
no datetime needed

leap year rules:
    if divisible by 4
        unless divisible by 100
            unless divisible by 400

Algorithm for is_leap_year:
     if year % 4 and ( not year % 100 or year % 400):
        return true
    return false

Algorithm for month_length:
    if month == 2:
        if leap_year(year)
            return 29
        else
            return 28
    else if month in [4,6,9,11]:
        return 30
    return 31

Algorithm for leap_years_until:
    return (year // 4 - year // 100) + year // 400

algorithm for year_to_days:
    return leap_years_since(year) + (year * 365)

algorithm for day of week:
    1753 == jan 1st, Monday

OR:
that's too much, so I found

Zeller's Congruence Algorithm

Weekday = (
            Monthday
            + ((13 (Month + 1) // 5)
            + (Year % 100)
            + ((Year % 100) // 4)
            + ((Year // 100) // 4)
            - ((Year // 100) * 5)
            )
            % 7

"""


DAYS_OF_WEEK = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday"]


def get_day_of_week(day:int, month:int, year:int):
    # Zeller Congruence
    if month == 1:
        month = 13
        year -= 1
    if month == 2:
        month = 14
        year -= 1
    y_mod = year % 100
    y_floor = year // 100

    day_of_week = (day
                      + ((13 * (month + 1)) // 5)
                      + y_mod + (y_mod // 4)
                      + (y_floor // 4)
                      + (y_floor * 5)
                   ) % 7

    return day_of_week

def friday_the_13ths(year):
    count = 0
    for i in range(1,13):
        if get_day_of_week(13, i, year) == 6:
            count += 1
    return count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True