#!/usr/bin/python
# -*- coding: utf-8 -*-


# 和单链表一样
class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkList(object):
    """单向循环链表"""

    # 变
    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    # 不变
    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    # 变
    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self.__head
        # count记录数量
        count = 1  # 计数从1，因为依据下述的循环条件，cur走到尾节点时不进入循环，此时count值不包含尾节点
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    # 变
    def travel(self):
        """遍历整个链表"""

        if self.is_empty():
            return
        cur = self.__head
        # 若链表为空，则cur.next不存在，循环会出问题，故先判断是否为空链表
        while cur.next != self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 当cur指向尾节点时即退出循环，故尾节点此时并未进行打印，下述语句打印尾节点
        print(cur.elem)

    # 变
    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        # 先判断链表是否为空，若为空执行if内语句
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # 链表不为空，创建一个游标找到其尾部节点
            cur = self.__head

            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    # 变
    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        # 先判断链表是否为空，为空执行if语句
        if self.is_empty():
            self.__head = node
            node.next = self.__head  # 改动
        else:
            # 链表不为空
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next  # 改动
            cur.next = node  # 改动

    # 和单链表的一样
    def insert(self, pos, item):
        """指定位置添加元素
        :param  pos 从0开始
        """
        node = Node(item)
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 从中间部分插入与单链表一致，故无需进行改变
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置

            node.next = pre.next
            pre.next = node

    # 变
    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        if self.is_empty():
            # 判断链表是否为空
            self.__head = None
            return
        while cur.next != self.__head:
            # 遍历链表
            if cur.elem == item:
                # 先判断cur是否等于item

                if cur == self.__head:
                    # 判断相等的节点是否是头节点
                    # 删除头节点，先增加一个游标mov指向尾节点
                    mov = self.__head
                    while mov.next != self.__head:
                        mov = mov.next
                    self.__head = cur.next
                    mov.next = self.__head
                else:  # 中间节点
                    pre.next = cur.next
                return    # 用return退出函数,用break退出的仅是循环
            else:
                pre = cur
                cur = cur.next
        # 跳出循环，cur指向尾节点
        if cur.elem == item:
            if cur == self.__head:
                # 判断是否仅一个节点
                self.__head = None
            else:
                pre.next = cur.next

    # 变
    def search(self, item):
        """查找节点是否存在"""
        # 先判断是否空链表
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next != self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            # 判断尾节点是否等于查询的参数
            if cur.elem == item:
                return True
            return False


if __name__ == "__main__":
    ll = SingleCycleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.travel()
    ll.add(8)
    ll.travel()
    ll.append(3)
    ll.add(4)
    ll.append(5)
    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 100)
    ll.travel()
    ll.insert(10, 200)
    ll.travel()
    ll.remove(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(200)
    ll.travel()
    print(ll.search(8))
