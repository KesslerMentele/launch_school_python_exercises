from datetime import date, timedelta


class Meetup:

    def __init__(self, year, month):
        self._year = year
        self._month = month

    def day(self, day, ordinal)->None | date:
        ord_number = {
            'first': 0,
            'second': 1,
            'third': 2,
            'fourth': 3,
            'fifth': 4,
            'last': -1
        }
        day_number = {
            'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday': 4,
            'saturday': 5,
            'sunday': 6,
        }

        ordinal = ordinal.casefold()
        days = self._get_all_of_weekday(day_number[day.casefold()])
        if ordinal in ord_number:
            if ord_number[ordinal] + 1 > len(days):
                return None
            return date(self._year, self._month, days[ord_number[ordinal]])
        if ordinal == 'teenth':
            return date(self._year, self._month,
                        [day for day in days if 12 < day < 20][0])
        return None

    def _get_all_of_weekday(self, day):
        day_numbers = []
        for i in range(1, self._get_month_length() + 1):
            if date(self._year, self._month, i).weekday() == day:
                day_numbers.append(i)
        return day_numbers

    def _get_month_length(self):
        new_date = date(self._year, (self._month % 12) + 1, 1)
        new_date += timedelta(days=-1)
        return new_date.day