# Bannerizer


def print_in_box(message):
    dashes = len(message) + 2
    print(f'+{'-' * dashes}+')
    print(f'|{' ' * dashes}|')
    print(f'| {message} |')
    print(f'|{' ' * dashes}|')
    print(f'+{'-' * dashes}+')



print_in_box('To boldly go where no one has gone before.')

print_in_box('')