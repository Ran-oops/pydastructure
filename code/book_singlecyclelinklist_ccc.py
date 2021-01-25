
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.pnext = None

    def __repr__(self):  # 这个函数将内容‘友好’地显示出来，否则会显示对象的内存地址
        return str(self.elem)


class LCList:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        """
        判断该链表是否为空
        :return: boolean
        """
        return self.rear == None

    def prepend(self, elem):  # 前端插入
        p = Node(elem)
        if self.rear is None:
            p.pnext = p  # 建立一个结点的环
            self.rear = p
        else:
            p.pnext = self.rear.pnext
            self.rear.pnext = p

    def append(self, elem):  # 尾端插入
        self.prepend(elem)
        self.rear = self.rear.pnext

    def pop_start(self):  # 前端弹出
        if self.rear is None:
            print("The list is None.")
            return
        p = self.rear.pnext
        if self.rear is p:  # 如果只有一个元素
            self.rear = None
        else:
            self.rear.pnext = p.pnext  # 令rear的指针等于第二个元素的地址
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self.rear.pnext
        print("Head", end=' ')
        while True:
            print("-->", p.elem, end=' ')
            if p is self.rear:
                break
            p = p.pnext
        print("--> None. Linked node finished")


if __name__ == '__main__':
    node1 = Node(elem='node1')
    node2 = Node(elem='node2')
    lclist = LCList()
    lclist.append(node1)
    lclist.append(node2)
    lclist.printall()
    print(lclist.pop_start())
    lclist.printall()