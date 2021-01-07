#!/usr/bin/python
# -*- coding: utf-8 -*-

class NotIterable(object):
    def __init__(self, baselist):
        self._baselist = baselist

    def __getitem__(self, index):
        # print("hhhhhhhhhhh")
        # print("index-----", index)
        return self._baselist[index]


t = NotIterable([1, 2, 3])
print(type(t), dir(t))
for i in t:
    print(i)

"""

什么是Iterable(可迭代对象)？
    1. 实现了__iter__方法，并返回迭代器的对象；
    2. 或者实现了__getitem__方法，并且可以通过下标从0开始依次取值的对象；取值结束后抛出IndexError；

什么是Iterator(迭代器)？
    1. 实现了next()方法或者__next__()的对象

如果迭代器不实现__iter__方法的话,上述函数和工具都无法用来对迭代器进行迭代,只能通过人工调用next()方法来进行迭代,这与python"简洁统一"的设计原则相违背,所以迭代器要实现
__iter__方法
"""


# class Fib(object):
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     # def __next__(self):
#     #     self.a , self.b = self.b , self.a + self.b
#     #     return self.a
#
#     def __iter__(self):
#         return self
#
#
# for i in Fib():
#     print(i)



