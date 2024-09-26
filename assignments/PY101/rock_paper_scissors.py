import random

VALID_CHOICES = ['scissors', 'paper', 'rock'] # 'lizard', 'spock', 'dynamite']
# This will work with any number of valid choices.
# Where a choice will:
# Win to any choice an odd number of indices in front,
# and win to any even number of indices away behind
# else it will lose


MIN_BRIGHTNESS = 650


def enforce_min_brightness(r, g, b):
    current_brightness = r + g + b

    if current_brightness >= MIN_BRIGHTNESS:
        return r, g, b

    scale_factor = MIN_BRIGHTNESS / current_brightness

    r = min(int(r * scale_factor), 255)
    g = min(int(g * scale_factor), 255)
    b = min(int(b * scale_factor), 255)

    return r, g, b


def get_colors(count):
    color_list = []
    for _ in range(count):
        r = random.randint(25, 255)
        g = random.randint(25, 255)
        b = random.randint(25, 255)
        r, g, b = enforce_min_brightness(r, g, b)
        color_list.append(f"\033[38;2;{r};{g};{b}m")

    return color_list

colors  = get_colors(len(VALID_CHOICES))

def colorize_text(text):
    for word, color in zip(VALID_CHOICES, colors):
        text = text.replace(word, f"{color}{word}\033[0m")
    return text

def prompt(message):

    print(f"==> {colorize_text(message)}")


def ask(message):
    return input(f"==> {colorize_text(message)}\n")


def determine_winner(player_1, player_2):
    index_1 = VALID_CHOICES.index(player_1)
    index_2 = VALID_CHOICES.index(player_2)

    if index_1 == index_2:
        return f"You both chose {player_1}. It's a tie!"

    if index_1 > index_2:
        if (index_1 - index_2) % 2 == 0:
            return f"{player_1} beats {player_2}! You win!"
        return f"{player_2} beats {player_1}! You lose!"
    if (index_2 - index_1) % 2 == 0:
        return f"{player_2} beats {player_1}! You lose!"
    return f"{player_1} beats {player_2}! You win!"


def rock_paper_scissors():
    replay = ''
    while replay != 'n':
        replay = ''
        choice = ask(f"Choose one: {', '.join(VALID_CHOICES)}")
        while choice.casefold() not in VALID_CHOICES:
            prompt('That isn\'t an option!')
            choice = ask(f"Choose one: {', '.join(VALID_CHOICES)}")
        computer_choice = random.choice(VALID_CHOICES)
        prompt(f"You chose {choice}, the computer chose {computer_choice}")
        winner = determine_winner(choice, computer_choice)
        prompt(winner)
        while replay not in ['y', 'n','s']:
            replay = ask("Play again? (Y/N)").casefold()



rock_paper_scissors()