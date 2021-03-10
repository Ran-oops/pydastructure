# coding: utf-8


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootval(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.getRootval())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree, num):
    if tree is not None:
        postorder(tree.getLeftChild(), num)
        print("lllnum====", num)
        postorder(tree.getRightChild(), num)
        print("rrrrnum====", num)
        print(tree.getRootval())

        return num

def midorder(tree):
    if tree is not None:
        midorder(tree.getLeftChild())
        print(tree.getRootval())
        midorder(tree.getRightChild())


if __name__ == '__main__':
    r = BinaryTree("a")
    r.insertLeft("d")
    # r.insertLeft("b")
    r.insertRight("c")
    # r.getRightChild().setRootVal("hello")
    # print(r.getRightChild().key)
    # print(r.getLeftChild().key)
    # print(r.getLeftChild().getLeftChild().key)
    print(postorder(r, 0))