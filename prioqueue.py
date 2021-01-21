class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)


    def enqueue(self, e):
        i = len(self._elems) - 1
        # while i >= 0:
        #     if self._elems[i] <= e:
        #         i -= 1
        #     else:
        #         break
        # self._elems.insert(i + 1, e)
        while self._elems[i] <= e:
            i -= 1
        self._elems.insert(i+1, e)
        print(self._elems)

p = PrioQue(elist=[2,5,1,0])
p.enqueue(-1)