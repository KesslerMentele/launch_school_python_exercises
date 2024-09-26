import random

VALID_CHOICES = ['scissors', 'paper', 'rock', 'lizard', 'spock', 'dynamite', 'spork']
# This will work with any number of valid choices.
# Where a choice will:
# Win to any choice an odd number of indices in front,
# and win to any even number of indices away behind
# else it will lose

MIN_BRIGHTNESS = 400



colors  = []

def create_identifiers():
    index = 0
    identifiers = []

    while index < len(VALID_CHOICES):
        char_index = 0
        identifier = ''

        while char_index < len(VALID_CHOICES[index]):
            identifier += VALID_CHOICES[index][char_index]
            if identifier not in identifiers:
                identifiers.append(identifier)
                break
            char_index += 1
        index += 1
    return identifiers


typeable_options = create_identifiers()

formatted_choices = [f"{choice} ({option})" for choice, option in
                     zip(VALID_CHOICES, typeable_options)]


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


def colorize_text(text):
    for word, color in zip(VALID_CHOICES, colors):
        text = text.replace(word, f"{color}{word}\033[0m")
    return text


def prompt(message):

    print(f"==> {colorize_text(message)}")


def ask(message):
    return input(f"==> {colorize_text(message)}\n")


def determine_round_winner(player_1, player_2):
    index_1 = VALID_CHOICES.index(player_1)
    index_2 = VALID_CHOICES.index(player_2)

    if index_1 == index_2:
        return f"You both chose {player_1}. It's a tie! No points!", None

    if index_1 > index_2:
        if (index_1 - index_2) % 2 == 0:
            return f"{player_1} beats {player_2}! You win the round!", 0
        return f"{player_2} beats {player_1}! You lose the round!", 1
    if (index_2 - index_1) % 2 == 0:
        return f"{player_2} beats {player_1}! You lose the round!", 1
    return f"{player_1} beats {player_2}! You win the round!", 0


def game_loop():
    scores = [0, 0]
    while not any(value == 3 for value in scores ):
        choice = ask(f"Choose one: {', '.join(formatted_choices)}")
        while choice.casefold() not in typeable_options:
            prompt('That isn\'t an option!')
            choice = ask(f"Choose one: {', '.join(formatted_choices)}")
        choice_index = typeable_options.index(choice)
        choice = VALID_CHOICES[choice_index]

        computer_choice = random.choice(VALID_CHOICES)
        prompt(f"You chose {choice}, the computer chose {computer_choice}")
        winner, point = determine_round_winner(choice, computer_choice)
        if point:
            scores[point] += 1
        prompt(winner)
    if scores[0] == 3:
        return "And that's 3 points to you, you win!"
    return "And that's 3 points to the computer, you lose!"



def rock_paper_scissors():
    global colors
    colors = get_colors(len(VALID_CHOICES))
    replay = ''



    while replay != 'n':
        replay = ''
        result = game_loop()
        prompt(result)
        while replay not in ['y', 'n','s']:
            replay = ask("Good game! Play again? (Y/N)").casefold()



rock_paper_scissors()