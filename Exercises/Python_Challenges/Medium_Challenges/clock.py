


class Clock:
    _MINUTES_IN_DAY = 1440

    def __init__(self, minute):
        while minute < 0:
            minute += self._MINUTES_IN_DAY
        minute %= self._MINUTES_IN_DAY
        self._minute = minute


    @staticmethod
    def at(hours, minutes=0):
        time = ((hours * 60) + minutes) % Clock._MINUTES_IN_DAY
        return Clock(time)

    def __str__(self):
        return f"{str(self._minute // 60).rjust(2, '0')}:{str(self._minute % 60).rjust(2, '0')}"

    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Clock(self._minute + other)

    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Clock(self._minute - other)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return self._minute == other._minute
