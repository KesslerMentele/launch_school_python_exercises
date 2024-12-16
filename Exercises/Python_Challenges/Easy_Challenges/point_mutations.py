#
# Compute the hamming distance of two strings
# If the strings are of unequal length, stop when the shorter sting ends
#
#
#
#
#


class DNA:

    def __init__(self, strand):
        self.value = strand

    def hamming_distance(self, other):
        if not isinstance(other, str):
            raise TypeError('Must be a string!')

        distance = 0

        shortest = min([len(self.value), len(other)])
        for i in range(shortest):
            if self.value[i] != other[i]:
                distance += 1

        return distance

