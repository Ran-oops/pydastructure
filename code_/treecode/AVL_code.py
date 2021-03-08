# coding: utf-8

import bst_code

"""
平衡因子在-1, 0, 1之间,这个二叉搜索树就被称为平衡树
平衡二叉查找树: 既平衡又满足BST的性质
h(层数,搜索次数) = 1.44logNh
最多搜索次数h和规模N的关系,可以说AVL树的搜索时间复杂度为O(logn)

经过复杂的put方法,AVL树始终维持平衡,get方法也始终保持O(logn)
AVL树的put方法分为两个部分:
1. 需要插入的新节点是叶节点,更新其所有父节点和祖先结点的代价最多为O(logn)
2. 如果插入的新节点引发了不平衡,重新平衡最多需要2次旋转,但旋转的代价与问题规模无关,
是常数O(1), 所以整个put方法的时间复杂度还是O(logn)
"""


class BalancedBinaryTree(bst_code.BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftchild)
            else:
                currentNode.leftchild = bst_code.TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftchild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightchild)
            else:
                currentNode.rightchild = bst_code.TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightchild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightchild
        rotRoot.rightchild = newRoot.leftchild
        # print(newRoot.key)
        if newRoot.leftchild is not None:
            newRoot.leftchild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftchild = newRoot
            else:
                rotRoot.parent.rightchild = newRoot
        newRoot.leftchild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        newRoot = rotRoot.leftchild
        rotRoot.leftchild = newRoot.rightchild
        if newRoot.rightchild is not None:
            newRoot.rightchild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightchild = newRoot

        newRoot.rightchild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
                                1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
                                1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        """
        如果子树需要左旋,首先检查右子树的平衡因子,如果右子树左倾,需要对右子树做一次右旋,
        再围绕原结点做一次左旋.
        如果子树需要右旋,首先检查左子树的平衡因子,如果左子树右倾,需要对左子树做一次左旋,
        再围绕原结点做一次右旋.
        """
        # 右倾
        if node.balanceFactor < 0:

            if node.rightchild.balanceFactor > 0:
                # Do an LR Rotation
                self.rotateRight(node.rightchild)
                self.rotateLeft(node)
            else:
                # single left
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftchild.balanceFactor < 0:
                # Do an RL Rotation
                self.rotateLeft(node.leftchild)
                self.rotateRight(node)
            else:
                # single right
                self.rotateRight(node)


if __name__ == '__main__':
    avl_tree = BalancedBinaryTree()
    # avl_tree[10] = "zhangsan"
    # avl_tree[20] = "lisi"
    # avl_tree[30] = "lisi"
    # avl_tree[40] = "lisi"
    # avl_tree[50] = "lisi"
    # avl_tree[9] = "three"
    # avl_tree[6] = "two"
    # avl_tree[10] = "four"
    #
    # avl_tree[8] = "one"
    # avl_tree[7] = "five"
    # avl_tree[8.2] = "point"
    avl_tree[18] = "18"
    avl_tree[33] = "33"
    avl_tree[55] = "55"
    avl_tree[66] = "66"
    avl_tree[99] = "99"
    # for i in avl_tree:
    #     print(i)
    print(avl_tree.height())
