

class Element:
    def __init__(self, datum, next=None):
        self._datum = datum
        self._next = next

    @property
    def datum(self):
        return self._datum

    @property
    def next(self):
        return self._next

    def is_tail(self):
        return self.next is None


class SimpleLinkedList:
    def __init__(self):
        self._itm = None

    @property
    def size(self):
        cur_itm = self._itm
        count = 0
        while cur_itm:
            cur_itm = cur_itm.next
            count += 1
        return count

    @property
    def head(self):
        return self._itm

    def is_empty(self):
        return self._itm is None

    def peek(self):
        if self.is_empty():
            return None
        return self._itm.datum

    def push(self, datum):
            self._itm = Element(datum, next=self._itm)

    def pop(self):
            to_pop, self._itm = self._itm, self._itm.next
            return to_pop.datum

    @staticmethod
    def from_list(lst:list | None):
        if not lst:
            return SimpleLinkedList()
        copy_list = lst.copy()
        new_linked_list = SimpleLinkedList()
        while copy_list:
            new_linked_list.push(copy_list.pop())
        return new_linked_list

    def to_list(self):
        new_list = []
        cur_itm = self._itm
        while cur_itm:
            new_list.append(cur_itm.datum)
            cur_itm = cur_itm.next
        return new_list

    def reverse(self):
        return SimpleLinkedList.from_list(self.to_list()[::-1])


