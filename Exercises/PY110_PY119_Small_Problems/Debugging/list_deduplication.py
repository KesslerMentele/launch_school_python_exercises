"""
The problem is that the set type is an unordered collection. Instead we can
create a set of data that had been added by iterating through the items like
so:
"""


data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
data_filter = set()
unique_data = []
for item in data:
    if item not in data_filter:
        unique_data.append(item)
        data_filter.add(item)

print(unique_data == [4, 2, 1, 3]) # order not guaranteed