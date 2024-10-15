def calculate_pyramid(max_cubes_count):
    layer = 1
    sum_of_squares = 0
    while True:
        layer_count = layer ** 2
        if (sum_of_squares + layer_count) > max_cubes_count:
            remainder = max_cubes_count - sum_of_squares
            return remainder
        sum_of_squares += layer_count
        layer += 1


# I also wrote a faster approximation with time complexity O(1)
# It fails with cube counts more than 16 digits long, but I think its close
# enough for how much faster it is.

def get_fast_remainder(cubes):
    # Fails with numbers > 1 * 10 ^ 19
    layers = (3 * cubes) ** (1. / 3)
    layers = int(layers)
    print(layers)
    layer_count_one = (layers * (layers + 1) * ((layers * 2) + 1)) / 6
    if layer_count_one <= cubes:

        return cubes - layer_count_one
    layer_two = layers - 1
    layer_count_two = (layer_two * (layer_two + 1) * ((layer_two * 2) + 1)) / 6
    return cubes - layer_count_two

print(calculate_pyramid(0) == 0)  # True
print(calculate_pyramid(1) == 0)  # True
print(calculate_pyramid(2) == 1)  # True
print(calculate_pyramid(4) == 3)  # True
print(calculate_pyramid(5) == 0)  # True
print(calculate_pyramid(6) == 1)  # True
print(calculate_pyramid(14) == 0) # True