

# Problem 1
def problem_one():
    fruits = ("apple", "banana", "cherry", "date", "banana")
    bananas = 0
    for item in fruits:
        if item == "banana":
            bananas += 1
    return bananas


# Problem 3
def problem_three():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    unique = a | b
    print(unique)


# Problem 5
def problem_five():
    ages = {
        "Herman": 32,
        "Lily": 30,
        "Grandpa": 5843,
        "Eddie": 10,
        "Marilyn": 22,
        "Spot": 237,
    }
    total_age = 0
    for age in ages.values():
        total_age += age
    print(total_age)


# Problem 6
def problem_six():
    ages = {
        "Herman": 32,
        "Lily": 30,
        "Grandpa": 5843,
        "Eddie": 10,
        "Marilyn": 22,
        "Spot": 237,
    }
    smallest_age = min(ages.values())
    print(smallest_age)


# Problem 8
def problem_eight():
    statement = "The Flintstones Rock"
    character_count = {}
    for char in [char for char in statement if not char.isspace()]:
            character_count[char] = 1 if char not in character_count.keys() else character_count[char] + 1
    print(character_count)

# Problem


# list[a:b:c]
# length =  |(b - a) // c|