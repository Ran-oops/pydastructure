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














































































































