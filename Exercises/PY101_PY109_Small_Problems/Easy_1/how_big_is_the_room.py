# How big is the room?

def get_length():
    length = input('How long is the room, in meters?')
    try:
        return float(length)
    except ValueError:
        print('please input only the number as a whole number or decimal, no units')
        return get_length()

def get_width():
    width = input('How wide is the room, in meters?')
    try:
        return float(width)
    except ValueError:
        print(
            'please input only the number as a whole number or decimal, no units')
        return get_length()

def how_big():
    length = get_length()
    width = get_width()
    area_meters = length * width
    area_feet = area_meters * 10.7639
    print(f'The room is: \n {area_meters} square meters \n or \n {area_feet} square feet')

how_big()