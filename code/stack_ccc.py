# coding: utf-8


class Stack(object):
    def __init__(self, limit=10):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    # 返回栈顶元素
    def peek(self):
        if self.__items:
            return self.__items[-1]
        else:
            return None

    def size(self):
        return len(self.__items)

    def push(self, item):
        self.__items.append(item)

    # 弹出栈顶元素
    def pop(self):
        if len(self.__items) <= 0:
            return -1
        else:
            return self.__items.pop()


if __name__=="__main__":
    myStack = Stack()
    myStack.push(1)
    myStack.push(3)
    myStack.push(5)
    myStack.push(7)
    myStack.push(8)
    # print(myStack.size())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    # myStack.pop()
    # myStack.pop()
    # print(myStack.size())
