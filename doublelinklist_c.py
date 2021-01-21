#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
双向链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""
"""
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
"""

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next_ = None
        self.prev = None

class DoubleLinkList(object):
    """单链表"""
    def __init__(self):
        # 这个(属性)变量指向头结点, 现在为None表示没有头结点,是空链表
        # 有了这个属性才能把头结点保存下来 然后把之后的结点都串起来
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self.__head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点, 当前结点的下一结点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node
            node.next.prev = node
            # self.__head.prev = node
            # node.next = self.__head
            # # 将链表的头_head指向新节点
            # self.__head = node


    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self.__head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self.__head             # 获取现在最后的那个节点
            print("cur=====", cur)
            while cur.next != None:       # 若不为空,则找到尾部,将尾结点的next指向新节点
                cur = cur.next
            cur.next = node
            node.prev = cur


    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = Node(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            cur = self.__head
            while count < pos:
                count += 1
                cur = cur.next
            # 当循环退出后,cur指向pos位置
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if cur == self.__head:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                    # 将当前结点的prev设为None
                    # 处理链表只有一个结点的特殊情况
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    # 处理待删除结点是最后一个结点的情况
                    if cur.next:
                        cur.next.prev = cur.prev
                break
            else:
                # 继续按链表后移节点
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False