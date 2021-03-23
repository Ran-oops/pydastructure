# coding: utf-8


# def binarytree(r):
#     return [r, [], []]
#
#
# def insertleft(root, newbranch):
#     t = root.pop(1)
#     root.insert(1, [newbranch, t, []])
#     return root
#
#
# def inserRight(root, newbranch):
#     t = root.pop(2)
#     root.insert(2, [newbranch, [], t])
#     return root
#
#
# def getleft(root):
#     return root[1]
#
#
# def getright(root):
#     return root[2]
#
#
# def setrootval(root, val):
#     root[0] = val
#     return root
#
#
# def getrootval(root):
#     return root[0]


# class BinaryTree:
#     def __init__(self, rootobj):
#         self.key = rootobj
#         self.leftchild = None
#         self.rightchild = None
#
#     def insertleft(self, newnode):
#         if self.leftchild is None:
#             self.leftchild = BinaryTree(newnode)
#         else:
#             t = BinaryTree(newnode)
#             t.leftchild = self.leftchild
#             self.leftchild = t
#
#     def insertright(self, newnode):
#         if self.rightchild is None:
#             self.rightchild = BinaryTree(newnode)
#         else:
#             t = BinaryTree(newnode)
#             t.rightchild = self.rightchild
#             self.rightchild = t
#
#     def getleftchild(self):
#         return self.leftchild
#
#     def getrightchild(self):
#         return self.rightchild
#
#     def setrootval(self, rootval):
#         self.key = rootval
#
#     def getrootval(self):
#         return self.key
#
#
# def preorder(tree):
#     if tree:
#         print(tree.getrootval())
#         preorder(tree.getleftchild())
#         preorder(tree.getrightchild())
#
#
# def postorder(tree):
#     if tree:
#         postorder(tree.getleftchild())
#         postorder(tree.getrightchild())
#         print(tree.getrootval())


# def midorder(tree):
#     if tree:
#         midorder(tree.getleftchild())
#         print(tree.getrootval())
#         midorder(tree.getrightchild())

"""
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def perup(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perup(self.currentSize)
"""

# class BinHeap:
#     def __init__(self):
#         self.currentsize = 0
#         self.heapList = [0]
#
#     def perup(self, i):
#         while i//2 > 0:
#             if self.heapList[i] < self.heapList[i//2]:
#                 self.heapList[i], self.heapList[i//2] = self.heapList[i//2], self.heapList[i]
#             i = i // 2
#
#     def perdown(self, i):
#         while i*2 <= self.currentsize:
#             mc = self.minchild(i)
#             if self.heapList[i] > self.heapList[mc]:
#                 self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
#             i = mc
#
#     def minchild(self, i):
#         if i*2 + 1 > self.currentsize:
#             return i*2
#         else:
#             if self.heapList[i*2] > self.heapList[i*2+1]:
#                 return i*2+1
#             else:
#                 return i*2
#
#     def insert(self, k):
#         self.heapList.append(k)
#         self.currentsize = self.currentsize + 1
#         self.perup(self.currentsize)
#
#     def delmin(self):
#         retval = self.heapList[1]
#         self.heapList[1] = self.heapList[self.currentsize]
#         self.currentsize = self.currentsize - 1
#         self.heapList.pop()
#         self.perdown(1)
#         return retval
#
#     def buildheap(self, alist):
#         self.currentsize = len(alist)
#         self.heapList = [0] + alist[:]
#         i = self.currentsize // 2
#         while i > 0:
#             self.perdown(i)
#             i -= 1



# class BinarySearchTree:
#     def __init__(self):
#         self.root = None
#         self.size = 0
#
#     def length(self):
#         return self.size
#
#     def __len__(self):
#         return self.size
#
#     def __iter__(self):
#         return self.root.__iter__()
#
#     def height(self):
#         return self.root.height()
#
#
# class TreeNode:
#     def __init__(self, key, val, left=None, right=None, parent=None):
#         self.key = key
#         self.payload = val
#         self.leftchild = left
#         self.rightchild = right
#         self.parent = parent
#         self.balancefactor = 0
#
#     def hasLeftChild(self):
#         return self.leftchild
#
#     def hasRightChild(self):
#         return self.rightchild
#
#     def isLeftChild(self):
#         return self.parent and self.parent.leftchild == self
#
#     def isRightChild(self):
#         return self.parent and self.parent.rightchild == self
#
#     def isRoot(self):
#         return not self.parent
#
#     def isLeaf(self):
#         return not (self.leftchild or self.rightchild)
#
#     def hasAnyChildren(self):
#         return self.leftchild or self.rightchild
#
#     def hasBothChildren(self):
#         return self.rightchild and self.leftchild
#
#     def replaceNodeData(self, key, val, lc, rc):
#         self.key = key
#         self.payload = val
#         self.leftchild = lc
#         self.rightchild = rc
#         if self.hasLeftChild():
#             self.leftchild.parent = self
#         if self.hasRightChild():
#             self.rightchild.parent = self
#
#     def __iter__(self):
#         if self:
#             if self.hasLeftChild():
#                 for elem in self.leftchild:
#
#                     yield elem
#             yield self.key
#             if self.hasRightChild():
#                 for elem in self.rightchild:
#                     yield elem
#             yield self.key
#             if self.hasLeftChild():
#                 for elem in self.leftchild:
#                     yield elem
#
#     def findSuccessor(self):
#         succ = None
#         if self.hasRightChild():
#             succ = self.rightchild.findMin()
#         return succ
#
#     def findMin(self):
#         current = self
#         while current.hasLeftChild():
#             current = current.leftchild
#         return current
#
#     def spliceOut(self):
#         if self.isLeaf():

from pythonds.graphs import Graph


# class DFSGraph(Graph):
#     def __init__(self):
#         super().__init__()
#         self.time = 0
#
#     def dfs(self):
#         for aVertex in self:
#             aVertex.setColor('white')
#             aVertex.setPred(-1)
#         for aVertex in self:
#             if aVertex.getColor() == 'white':
#                 self.dfsvisit(aVertex)
#
#     def dfsvisit(self, startVertex):
#         startVertex.setColor('gray')
#         self.time += 1
#         startVertex.setDiscovery(self.time)
#         for nextVertex in startVertex.getConnections():
#             if nextVertex.getColor() == 'white':
#                 nextVertex.setPred(startVertex)
#                 self.dfsvisit(nextVertex)
#         startVertex.setColor('black')
#         self.time += 1
#         startVertex.setFinish(self.time)
#         print(startVertex.getId(), end= ' ')

# class DFSGraph(Graph):
#     def __init__(self):
#         super().__init__()
#         self.time = 0
#
#     def dfs(self):
#         for aVertex in self:
#             aVertex.setColor('white')
#             aVertex.setPred(-1)
#         for aVertex in self:
#             if aVertex.getColor() == 'white':
#                 self.dfsvisit(aVertex)
#
#     def dfsvisit(self, startVertex):
#         startVertex.setColor('gray')
#         self.time += 1
#         startVertex.setDiscovery(self.time)
#         for nextVertex in startVertex.getConnections():
#             if nextVertex.getColor() == 'white':
#                 nextVertex.setPred(startVertex)
#                 self.dfsvisit(nextVertex)
#         startVertex.setColor('black')
#         self.time += 1
#         startVertex.setFinish(self.time)


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


def binary_search(alist, item):
    n = len(alist)
    if n>0:
        mid = n // 2
        if alist[mid] == item:
            return True
        if item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            binary_search(alist[:mid], item)
        else:
            binary_search(alist[mid+1:], item)
    return False


def binary_search(alist, item):
    n = len(alist)
    if n > 0:
        mid = n // 2
        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            binary_search(alist[:mid], item)
        else:
            binary_search(alist[mid+1:], item)
    return False


def bubble_sort(alist):
    n = len(alist)
    count = 0
    for j in range(n-1):
        for i in range(0, n-1-j):
            if alist[i]> alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return

# def bubble_sort(alist):
#     n = len(alist)
#     count = 0
#     for j in range(n-1):
#         for i in range(0, n-1-j):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
#                 count += 1
#         if count == 0:
#             return

# def choose_sort(alist):
#     n = len(alist)
#     for j in range(n-1):
#         minu = j
#         for i in range(j+1, n):
#             if alist[i] < alist[minu]:
#                 alist[minu], alist[j] = alist[j], alist[minu]


def bubble_sort(alist):
    n = len(alist)
    count = 0
    for j in range(n-1):
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return


def choose_sort(alist):
    n = len(alist)
    for j in range(n-1):
        minu = j
        for i in range(j+1, n):
            if alist[i] < alist[minu]:
                minu = i
        alist[minu], alist[j] = alist[j], alist[minu]


def choose_sort(alist):
    n = len(alist)
    for j in range(n-1):
        minu = j
        for i in range(j+1, n):
            if alist[i] < alist[minu]:
                minu = i
        alist[minu], alist[j] = alist[j], alist[minu]


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        key = alist[i]
        while j > 0 and key < alist[j-1]:
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = key


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        key = alist[i]
        while j > 0 and key < alist[j-1]:
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = key


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        key = alist[j]
        while j > 0 and key < alist[j]:
            alist[j] = alist[j-1]
            j -= 1
        alist[j] = key


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

















































































