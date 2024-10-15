# Running Totals

def running_total(items):
    for i in range(1, len(items)):
        items[i] = items[i] + items[i - 1]
    return items

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True