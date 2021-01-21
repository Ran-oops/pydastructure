#!/usr/bin/python
# -*- coding: utf-8 -*-


# def reversedemo():
#     elements = [5, 2, 3, 7, 10, 9, 6]
#     j = len(elements) - 1
#     i = 0
#     print("index", j)
#     while i < j:
#         elements[j], elements[i] = elements[i], elements[j]
#         i, j = i+1, j-1
#
#     print(elements)
#
#
# reversedemo()
#
# print("========================")
#
# lst = [5, 2, 3, 7, 10, 9, 6]
# lst.reverse()
# print(lst)
# for i in range(2, 11):
#     print(i)


class SingleNode(object):
    def __init__(self, elem):
        self.elem = elem
        self.next_ = None

class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def add(self, elem):
        node = SingleNode(elem)
        node.next_ = self.__head
        self.__head = node

    def length(self):
        count = 0
        cur = self.__head
        while cur != None:
            count += 1
            cur = cur.next_
        return count

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next_

    def append(self, elem):
        node = SingleNode(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next_
            cur.next = node

    def insert(self, pos, elem):
        node = SingleNode(elem)
        if pos <= 0:
            self.add(elem)
        elif pos > (self.length()-1):
            self.append(elem)
        else:
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next_
            node.next_ = cur.next_
            cur.next_ = node

    def remove(self, elem):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == elem:
                if not pre:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, elem):
        cur = self.__head
        while cur != None:
            if cur.elem == elem:
                return True
            cur = cur.next_
        return False






















