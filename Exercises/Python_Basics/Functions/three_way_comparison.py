# Three-way Comparison

def compare_by_length(string_one, string_two):
    length_one = len(string_one)
    length_two = len(string_two)
    if length_one > length_two:
        return 1
    if length_two > length_one:
        return -1
    else:
        return 0


compare_by_length('patience', 'perseverance')  # -1
compare_by_length('strength', 'dignity')  # 1
compare_by_length('humor', 'grace')  # 0