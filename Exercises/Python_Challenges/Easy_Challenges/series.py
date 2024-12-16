# Input: string of digits
# Output: all possible consecutive digit strings of a specified length
# error if series is longer than string

# def slices
#   if len > len(series) throw error
#
#
#
#


class Series:
    def __init__(self, series_string):
        self._series = series_string


    def slices(self, length):
        if length > len(self._series):
            raise ValueError
        slice_list = []
        for i in range((len(self._series) - length) + 1):
            slice_list.append([int(char) for char in self._series[i: i + length]])
        return slice_list


