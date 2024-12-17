# Input: letter
# Output: A diamond with widest point as the letter, top and bottom points are 'A'


# cap
# LETTERS[row_num] + " " + (" " * row_count) + " " +  LETTERS[row_num]
# until letter is reached, then return "\n".join(array + array[::-1])
#
#
#
#

class Diamond:
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def make_diamond(middle_letter):
        half_row = Diamond.LETTERS.index(middle_letter.upper())
        diamond = []
        cap = (" " * half_row) + "A" + (" " * half_row) + '\n'
        diamond.append(cap)

        for idx in range(1, half_row + 1):
            side_space = " " * (half_row - idx)
            inner_space = " " + (" " * (idx - 1) * 2)
            line = (side_space + Diamond.LETTERS[idx] + inner_space +
                    Diamond.LETTERS[idx] + side_space + '\n')
            diamond.append(line)

        inverse = diamond[:-1]
        diamond.extend(inverse[::-1])

        return ''.join(diamond)
