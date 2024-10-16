# Convert a String to a Signed Number

def string_to_signed_integer(string:str):
    value = 0

    for i in range(len(string)):

        match string[-(i+1)]:
            case "1":
                value += 1 * (10**i)
            case "2":
                value += 2 * (10 ** i)
            case "3":
                value += 3 * (10 ** i)
            case "4":
                value += 4 * (10 ** i)
            case "5":
                value += 5 * (10 ** i)
            case "6":
                value += 6 * (10 ** i)
            case "7":
                value += 7 * (10 ** i)
            case "8":
                value += 8 * (10 ** i)
            case "9":
                value += 9 * (10 ** i)
            case "0":
                value += 0
            case "-" if i == (len(string) - 1):
                # added sign case for '-' as first character
                value *= -1

    return value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True