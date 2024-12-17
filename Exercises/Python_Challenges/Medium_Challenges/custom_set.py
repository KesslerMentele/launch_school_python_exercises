

class CustomSet:

    def __init__(self, iterable=None):
        self._items = []
        if iterable:
            for item in iterable:
                self.add(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def __eq__(self, other):
        if not isinstance(other, CustomSet):
            return NotImplemented
        return self.is_subset(other) and other.is_subset(self)

    def __contains__(self, item):
        return item in self._items

    def is_empty(self):
        return not self._items

    def is_subset(self, other):
        return all([item in other for item in self])

    def contains(self, item):
        return item in self

    def is_disjoint(self, other):
        return not self.intersection(other)

    def is_same(self, other):
        return self == other

    def add(self, item):
        if item not in self._items:
            self._items.append(item)

    def intersection(self, other):
        intersect = []
        for item in other:
            if item in self._items:
                intersect.append(item)
        return CustomSet(intersect)

    def difference(self, other):
        diffs = []
        for item in self:
            if item not in other:
                diffs.append(item)
        return CustomSet(diffs)

    def union(self, other):
        new_set = CustomSet(self)
        for item in other:
            new_set.add(item)
        return new_set

