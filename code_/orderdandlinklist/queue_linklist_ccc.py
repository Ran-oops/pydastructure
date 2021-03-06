# coding: utf-8

"""
用链表实现队列
最简单的单链表只支持首端高效操作,在另一端操作需要O(n)时间,不适合作为队列的实现基础

用带表尾指针的单链表,支持O(1)时间的尾端插入操作(加入),表首端的高效访问和删除(弹出),
是实现队列最好的方式
"""
