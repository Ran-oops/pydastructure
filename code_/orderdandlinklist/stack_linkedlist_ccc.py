# coding: utf-8

"""
用链表实现栈, 从表头添加O(1),从表头删除O(n),即表头作为栈顶,表尾作为栈底
"""
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next_ = next_


class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return not self._top

    def top(self):
        if self._top is None:
            return "_top is None"
        return self._top.elem

    def push(self, elem):
        lnode = LNode(elem)
        lnode.next_ = self._top
        self._top = lnode

    def pop(self):
        if self._top is None:
            return "_top is None"
        else:
            p = self._top
            self._top = self._top.next_
            print(p.elem)
            return p.elem



if __name__ == '__main__':
    ls = LStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)
    ls.pop()
    ls.pop()
    ls.pop()
    ls.pop()