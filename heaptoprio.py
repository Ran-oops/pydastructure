#!/usr/bin/python
# -*- coding: utf-8 -*-


class PrioQueueError:
    def __init__(self, el):
        pass


class PrioQueue:
    """
    implementing priority queues using heaps
    """

    def __init__(self, elist=[]):
        if elist is None:
            elist = []
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)  # add a dummy element
        self.shiftup(e, len(self._elems) - 1)

    def shiftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems

        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.shiftdown(e, 0, len(elems))
        return e0

    def shiftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        print(elems, i, j)
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        print("end=======", end)
        for i in range(end // 2, -1, -1):
            self.shiftdown(self._elems[i], i, end)


pq = PrioQueue(elist=[5, 7, 9, 10, 4])
print(pq.is_empty())
print(pq.peek())
