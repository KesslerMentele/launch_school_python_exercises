# What Century is That?

def century(year):
    century_number = (year // 100) + 1
    if str(year)[-2::] == '00': century_number -= 1
    ordinal = 'th'
    if str(century_number)[-2:-1] != '1':
        match str(century_number)[-1::]:
            case '1':
                ordinal = 'st'
            case '2' :
                ordinal = 'nd'
            case '3':
                ordinal = 'rd'

    return str(century_number) + ordinal


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True