# Last Element

def last(input_list):
    if type(input_list) is list:
        return input_list[-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars