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


# class SingleNode(object):
#     def __init__(self, elem):
#         self.elem = elem
#         self.next_ = None
#
# class SingleLinkList(object):
#     """单链表"""
#     def __init__(self):
#         self.__head = None
#
#     def is_empty(self):
#         return self.__head is None
#
#     def add(self, elem):
#         node = SingleNode(elem)
#         node.next_ = self.__head
#         self.__head = node
#
#     def length(self):
#         count = 0
#         cur = self.__head
#         while cur != None:
#             count += 1
#             cur = cur.next_
#         return count
#
#     def travel(self):
#         cur = self.__head
#         while cur != None:
#             print(cur.elem)
#             cur = cur.next_
#
#     def append(self, elem):
#         node = SingleNode(elem)
#         if self.is_empty():
#             self.__head = node
#         else:
#             cur = self.__head
#             while cur.next != None:
#                 cur = cur.next_
#             cur.next = node
#
#     def insert(self, pos, elem):
#         node = SingleNode(elem)
#         if pos <= 0:
#             self.add(elem)
#         elif pos > (self.length()-1):
#             self.append(elem)
#         else:
#             cur = self.__head
#             count = 0
#             while count < (pos-1):
#                 count += 1
#                 cur = cur.next_
#             node.next_ = cur.next_
#             cur.next_ = node
#
#     def remove(self, elem):
#         cur = self.__head
#         pre = None
#         while cur != None:
#             if cur.elem == elem:
#                 if not pre:
#                     self.__head = cur.next
#                 else:
#                     pre.next = cur.next
#                 break
#             else:
#                 pre = cur
#                 cur = cur.next
#
#     def search(self, elem):
#         cur = self.__head
#         while cur != None:
#             if cur.elem == elem:
#                 return True
#             cur = cur.next_
#         return False

# for i in range(6, 5):
#     print(i)

aa = [4,14,31,46,63,53,47,62,52,58,48,33,16,1,11,5,15,21,6,23,38,55,61,51,57,40,50,56,41,24,9,3,13,7,22,39,54,60,45,30,36,26,20,37,43,28,18,8,2,12,29,35,25,19,34,44,59,49,32,42,27,17,0,10]
print(len(aa))




















