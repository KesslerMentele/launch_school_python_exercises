# Divided by Two

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for number in numbers.values():
    half_numbers.append( number // 2)

print(half_numbers)