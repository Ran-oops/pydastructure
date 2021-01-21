#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
单链表的操作
is_empty() 链表是否为空
length() 链表长度
travel() 遍历整个链表
add(item) 链表头部添加元素
append(item) 链表尾部添加元素
insert(pos, item) 指定位置添加元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        # next不为None的时候 等于谁(结点)就表示指向哪个结点
        self.next = None


class SingleLinkList(object):
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
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        print("node.itemmm", node.item)
        print("node.nexttttt", node.next)
        print("self.__head", self.__head.next.item)
        node.next = self.__head
        # 将链表的头_head指向新节点
        self.__head = node
        print("self.__head ater====", self.__head)

    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
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
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self.__head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            # 当循环退出后,pre指向pos-1的位置
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == "__main__":
    ll = SingleLinkList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.add(1)
    ll.travel()
    # print("seppppppppppppppppppp")
    # ll.add(2)
    # ll.append(3)
    # ll.insert(2, 4)
    # print("length:",ll.length())
    # ll.travel()
    # print(ll.search(3))
    # print(ll.search(5))
    # ll.remove(1)
    # print("length:",ll.length())
    # ll.travel()

