# given a natural number (limit) and a set of numbers (bases)
# find the sum of all multiples of the bases that are less than the limit
# if limit is 20 and bases are {3,5}:
# multiples are 3,6,9,12,15,18 from 3 and 5,10 from 5 (do not count 15 twice)

# initialize mults_set
# For each base
#   intdiv limit by base to get max_mult
#   for range(1,max_mult) add to mults_set
# sum mults_set

# @classmethod sum_up_to with default bases {3,5}
# @classmethod calls @staticmethod get_sum
# init with *args of bases
# to function calls @staticmethod get_sum with bases from instance


class SumOfMultiples:

    def __init__(self, *args):
        self._bases = set(args if args else (3,5))

    def to(self, limit):
        return self._get_sum(self._bases, limit)

    @staticmethod
    def _get_sum(bases, limit):
        mult_set = {0}
        for base in bases:
            max_mult = limit // base
            for cur_mult in range(1, max_mult + 1):
                mult = cur_mult * base
                if mult < limit:
                    mult_set.add(mult)
        return sum(mult_set)

    @classmethod
    def sum_up_to(cls, limit):
        return cls._get_sum({3,5}, limit)

