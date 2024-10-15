# Internationalization 2

def extract_language(locale):
    language_code = locale.split('_')[0]
    return language_code

def extract_region(locale):
    region_code = locale.split('_')[1].split('.')[0]
    return region_code

def locale_greet(locale):
    language = extract_language(locale)
    country = extract_region(locale)

    match (language, country):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case ('fr', _):
            return 'Salut!'
        case ('pt', _):
            return 'Olá!'
        case ('de', _):
            return 'Hallo!'
        case ('sv', _):
            return 'Hej!'
        case ('af', _):
            return 'Haai!'





print(locale_greet('fr_FR.UTF-8'))       # Salut!
print(locale_greet('fr_CA.UTF-8'))       # Salut!
print(locale_greet('fr_MA.UTF-8'))       # Salut!

print(locale_greet('en_US.UTF-8'))       # Hey!
print(locale_greet('en_GB.UTF-8'))       # Hello!
print(locale_greet('en_AU.UTF-8'))       # Howdy!