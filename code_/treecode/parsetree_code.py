#!/usr/bin/env python
# -*-coding: utf -8-*-

from code_.orderdandlinklist.stack_orderdlist_ccc import Stack
import binarytree2
# from .binarytree2 import BinaryTree
import operator
"""
(3+(4*5))
全括号表达式要分解为单词Token列表
单词分为"()", "+-*/", 和操作数"0~9"这几类
左括号就是表达式的开始,而右括号是表达式的结束
['(', '3', '+', '(', '4', '*', '5', ')', ')']
创建表达式解析树的过程:
创建空树,当前节点是根节点
读入'(',创建了左节点,当前节点下移
读入'3',当前节点设置为3,上升到父节点
读入'+',当前节点设置为+,创建右子节点,当前节点下降
读入'(',创建左子节点,当前节点下降
读入'4',当前节点设置为4,上升到父节点
读入'*',当前节点设置为*,创建右子节点,当前节点下降
读入'5',当前节点设置为5,上升为父节点
读入')',上升到父节点
读入')',再上升到父节点

总结:
遇见'(', 就是创建左节点,节点下降
遇见'0~9', 就是设置当前节点为'0~9',并上升到父节点
遇见'+-*/', 就是设置当前节点为'+-*/', 创建右子节点并下降
遇见')',上升到父节点
"""

"""
创建解析树的过程中关键的是对当前节点的跟踪
创建左右节点可调用insertLeft/insertRight
当前节点设置可调用setRootVal
下降到左右子树可调用getLeftChild/getRightChild

但是,上升到父节点,没有方法支持,因此,我们可以用一个栈来记录跟踪父节点:
当前节点下降时,将下降前的节点push入栈,当前节点需要上升到父节点时,上
升到pop出栈的节点即可
"""


def buildParseTree(fpexp):
    fplist = fpexp.split()
    # print("fplist", fplist)
    pStack = Stack()
    eTree = binarytree2.BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

"""
求值函数evaluate的递归三要素:
1. 基本结束条件
2. 缩小规模: 将表达式树分为左子树,右子树,即为缩小规模
3. 调用自身: 分别调用evaluate计算左子树和右子树的值,然后将左右子树的值依根节点
的操作符进行计算
"""


def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    # # 缩小规模
    # leftC = parseTree.getLeftChild()
    # rightC = parseTree.getRightChild()
    # if leftC and rightC:
    #     fn = opers[parseTree.getRootval()]
    #     # 递归调用
    #     return fn(evaluate(leftC), evaluate(rightC))
    # else:
    #     # 基本结束条件
    #     return parseTree.getRootval()
    res1 = None
    res2 = None
    if parseTree:

        res1 = evaluate(parseTree.getLeftChild())
        res2 = evaluate(parseTree.getRightChild())

        if res1 and res2:
            return opers[parseTree.getRootval()](res1, res2)
        else:
            return parseTree.getRootval()


if __name__ == '__main__':
    # tree = buildParseTree("( 3 + ( 4 * 5 ) )")
    tree = buildParseTree("( 3 + ( 4 / 1 ) )")
    print(evaluate(tree))














