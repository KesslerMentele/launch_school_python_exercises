"""
Input: string of characters

Output: a dict with floats to two decimals as strings like so:
    {
    'lowercase': "",
    'uppercase': "",
    'neither':  "",
    }


"""


def letter_percentages(string:str)->dict:
    length = len(string)
    counts =  {
    'lowercase': 0,
    'uppercase': 0,
    'neither':  0,
    }

    for char in string:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1
        else:
            counts['neither'] += 1

    result = {key:"{:.2f}".format((val / length) * 100) for key, val in counts.items() }
    return result



expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
