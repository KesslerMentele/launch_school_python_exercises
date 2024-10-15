# First Element

def first(input_list):
    if type(input_list) is list:
        return input_list[0]
    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))  # Earth