# coding: utf-8


class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
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


def postorder(tree):
    if tree is not None:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootval())


def midorder(tree):
    if tree is not None:
        preorder(tree.getLeftChild())
        print(tree.getRootval())
        preorder(tree.getRightChild())


if __name__ == '__main__':
    r = BinaryTree("a")
    r.insertLeft("d")
    r.insertLeft("b")
    r.insertRight("c")
    r.getRightChild().setRootVal("hello")
    print(r.getRightChild().key)
    print(r.getLeftChild().key)
    print(r.getLeftChild().getLeftChild().key)
