# coding: utf-8

"""
双端队列: 具有队列和栈的性质的数据结构
双端队列中的元素可以从两端弹出,其限定插入和删除操作在表的两端进行,双端队列可以在队列任意一段入队和出队

要求两端的插入和弹出操作都是O(1)时间复杂度
    1. 双链表
    2. 循环表结构
"""
"""
下面使用顺序表实现双端队列
"""

class Deque:
    def __init__(self):
        self.__list = []

    def add_front(self, elem):
        self.__list.insert(0, elem)

    def add_rear(self, elem):
        self.__list.append(elem)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def is_empty(self):
        return not self.__list

    def size(self):
        return len(self.__list)

if __name__ == "__main__":
    dq = Deque()
    dq.add_front(1)
    dq.add_front(2)
    dq.add_front(3)
    # print(dq.pop_rear())
    # print(dq.pop_rear())
    # print(dq.pop_rear())
    print(dq.pop_front())
    print(dq.pop_front())
    print(dq.pop_front())


























