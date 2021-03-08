#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BinarySearchTree:
    """
    二叉查找树算法分析(以put为例):
    其性能决定因素在于二叉搜索树的高度,而其高度又受数据项key插入顺序的影响
    1. 如果key的列表是随机分布的话,那么大雨和小于根节点key的键值大致相等
    BST的高度就是Log2n,n是节点的个数,而且,这样的树就是平衡树,put方法性能为O(Log2n)

    2. 如果key列表分布极端情况就完全不同: 如果按照从小到大的顺序插入的话,这时候put方法的性能为O(n)
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftchild)
            else:
                currentNode.leftchild = \
                TreeNode(key,val, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightchild)
            else:
                currentNode.rightchild = \
                TreeNode(key, val, parent=currentNode)
        else:
            currentNode.payload = val
            self.size -= 1

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftchild)
        else:
            return self._get(key,currentNode.rightchild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                print("==============key",nodeToRemove.key)
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")
    
    def __delitem__(self, key):
        self.delete(key)


    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftchild:
                currentNode.parent.leftchild = None
            else:
                currentNode.parent.rightchild = None

        elif currentNode.hasBothChildren():
            """
            有两个子节点的删除：
             1. 找到后继节点
             2. 将该节点替换为后继节点
             3. 将后继节点删除
            
            """
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else:
            print("is888888888888")
            """
            要删除的该节点只有一个子节点
            1. 当前节点是左子节点--->改父子节点的引用
            2. 当前节点是右子节点--->改父子节点的引用
            3. 当前节点是根节点--->替换根节点的key, payload,leftchild和rightchild数据
            """
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.leftchild
                elif currentNode.isRightChild():
                    currentNode.leftchild.parent = currentNode.parent
                    currentNode.parent.rightchild = currentNode.leftchild
                else:
                    currentNode.replaceNodeData(currentNode.leftchild.key,\
                                                currentNode.leftchild.payload,
                                                currentNode.leftchild.leftchild,
                                                currentNode.leftchild.rightchild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.leftchild = currentNode.rightchild
                elif currentNode.isRightChild():
                    currentNode.rightchild.parent = currentNode.parent
                    currentNode.parent.rightchild =currentNode.rightchild
                else:
                    currentNode.replaceNodeData(currentNode.rightchild.key,\
                                                currentNode.rightchild.payload,
                                                currentNode.rightchild.leftchild,
                                                currentNode.rightchild.rightchild)




class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftchild = left
        self.rightchild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftchild

    def hasRightChild(self):
        return self.rightchild

    def isLeftChild(self):
        return self.parent and \
               self.parent.leftchild == self

    def isRightChild(self):
        return self.parent and \
               self.parent.rightchild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftchild or self.rightchild)

    def hasAnyChildren(self):
        return self.leftchild or self.rightchild

    def hasBothChildren(self):
        return self.rightchild and self.leftchild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftchild = lc
        self.rightchild = rc
        if self.hasLeftChild():
            self.leftchild.parent = self
        if self.rightchild():
            self.rightchild.parent = self

    def __iter__(self):
        """
        这里其实是应用递归调用
        for...in...来调用自身的__iter__方法
        """
        if self:
            if self.hasLeftChild():
                for elem in self.leftchild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightchild:
                    yield elem

    def findSuccessor(self):
        """
        找后继节点有三种情况：
        1.如果节点有右子节点-->后继节点就是右子树中最小的节点
        2. 无右子节点：
            1. 本身是左子节点，-->后继节点就是父节点
            2. 本身是右子节点，-->后继节点是除其本身外父节点的后继节点
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightchild.findMin()
        else:
            print("11111111111")
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightchild = None
                    succ = self.parent.findsuccessor()
                    self.parent.rightchild = self
        print("=========",succ.key)
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftchild
        return current

    # 删除找到的后继节点
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftchild = None
            else:
                self.parent.rightchild = None
        elif self.hasAnyChildren(): # 其实就是self.hasRightChild()  因为只可能有右孩子
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftchild = self.leftChild
                else:
                    self.parent.rightchild = self.leftchild
                self.leftchild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftchild = self.rightchild
                else:
                    self.parent.rightchild = self.rightchild
            self.rightchild.parent = self.parent

mytree = BinarySearchTree()

# mytree[3] = "red"
# mytree[3] = "blueeeeeeeeeeeeeeeeee"
# mytree[4] = "blue"
# mytree[6]="yellow"
# mytree[2]="at"
# print(mytree[3])
# print(3 in mytree)
# del mytree[3]
# print(mytree[2])
# for key in mytree:
#     print(key, mytree[key])

mytree[9] = "three"
mytree[6] = "two"
mytree[10] = "four"

mytree[8] = "one"
mytree[7] = "five"
mytree[8.2] = "point"


# for key in mytree:
#     print(key, mytree[key], )

print(mytree.root.key) # 9
print(mytree.root.leftchild.key) # 6
print(mytree.root.rightchild.key) # 10
print(mytree.root.leftchild.rightchild.key)
print(mytree.root.leftchild.rightchild.leftchild.key)
print(mytree.root.leftchild.rightchild.rightchild.key)
# del mytree[8]
























