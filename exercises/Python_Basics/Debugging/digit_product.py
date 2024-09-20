# Digit Product

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1 # set to 1 for multiplication, else return is always 0

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0