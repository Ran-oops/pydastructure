#!/usr/bin/python
# -*- coding: utf-8 -*-


class BTree:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    # 向左子树插入节点
    def insertLeft(self, value):
        self.left = BTree(value)
        return self.left

    # 向右子树插入节点
    def insertRight(self, value):
        self.right = BTree(value)
        return self.right

    # 输出节点数据
    def show(self):
        print(self.data)


# 先序遍历
def preOrder(node):
    if node.data:
        node.show()
        if node.left:
            preOrder(node.left)
        if node.right:
            preOrder(node.right)


# 中序遍历
def midOrder(node):
    if node.data:
        if node.left:
            midOrder(node.left)
        node.show()
        if node.right:
            midOrder(node.right)


# 后序遍历
def postOrder(node):
    if node.data:
        if node.left:
            postOrder(node.left)
        if node.right:
            postOrder(node.right)
        node.show()


'''
主程序
'''
if __name__ == '__main__':
    Root = BTree('Root')  # 构建树
    A = Root.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')
    print('*************************')
    print('Binary Tree pre-traversal')
    preOrder(Root)
    print('*************************')
    print('Binary Tree mid-traversal')
    midOrder(Root)
    print('*************************')
    print('Binary Tree post-traversal')
    postOrder(Root)