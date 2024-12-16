

# Natural Numbers are either:
#    abundant (sum(divisors) > value)
#    perfect  (sum(divisors) == value)
#    deficient (sum(divisors) < value)
#
#
#
#
#

class PerfectNumber:
    @staticmethod
    def classify(value):
        if value < 1:
            raise ValueError("Input must be a positive integer")
        divisors = [num for num in range(1,value // 2 + 1) if value % num == 0]
        aliquot = sum(divisors)
        if aliquot == value:
            return 'perfect'
        elif aliquot > value:
            return 'abundant'
        else:
            return 'deficient'
