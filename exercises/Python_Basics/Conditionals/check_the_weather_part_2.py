# Check the Weather, Part 2

weather = 'snowy'

match weather:
    case 'sunny':
        print('It\'s a beautiful day!')
    case 'rainy':
        print('Grab your umbrella')
    case 'snowy':
        print('Wear your boots')
    case _:
        print('Let\'s stay inside')