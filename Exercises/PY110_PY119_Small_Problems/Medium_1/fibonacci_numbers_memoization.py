

memo = {1:1,2:1}
def fibonacci(num:int)->int:
    if num <= 2 :
        return 1
    if num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]

print(fibonacci(1) == 1)  # True
print(fibonacci(2) == 1)  # True
print(fibonacci(3) == 2)  # True
print(fibonacci(4) == 3)  # True
print(fibonacci(5) == 5)  # True
print(fibonacci(6) == 8)  # True
print(fibonacci(12) == 144)  # True
print(fibonacci(20) == 6765)  # True