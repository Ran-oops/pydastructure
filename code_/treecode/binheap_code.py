#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from pythonds.trees.binheap import BinHeap
# bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(11)
#
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())
# print(bh.delMin())

"""
完全二叉树: 如果节点的下标为p,那么其左子节点下标为2p,右子节点为
2p+1, 其父节点下标为p//2
"""


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perup(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
                # self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perup(self.currentSize)
        print(self.heapList)

    def perdown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minchild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
            # else:
            #     break

    def minchild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delmin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.perdown(1)
        return retval

    def buildheap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while i>0:
            print(self.heapList, i)
            self.perdown(i)
            i = i-1


bh = BinHeap()
# bh.insert(5)
# bh.insert(7)
# bh.insert(3)
# bh.insert(10)
bh.buildheap([5,7, 3, 10])
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
print(bh.delmin())
