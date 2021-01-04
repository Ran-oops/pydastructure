# -*- coding:utf-8 -*-

# class A:
#     def __init__(jj):
#         print(type(jj))
#         jj['B'] = 'BB'
#         print("hhhhhhhh")
#         jj['D'] = 'DD'
#
#     def __setitem__(self, name, value):
#         print("__setitem__:Set %s Value %s" % (name, value))
#
#
# if __name__ == '__main__':
#     X = A()


"""
__setitem__(self,key,value)：该方法应该按一定的方式存储和key相关的value。在设置类实例属性时自动调用的。
__xxxitem__:使用 [''] 的方式操作属性时被调用
__setitem__:每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
__getitem__:当访问不存在的属性时会调用该方法
__delitem__:当删除属性时调用该方法

https://blog.csdn.net/weixin_33733810/article/details/93881052  Python魔术方法的一些总结归纳
"""


class TestDemo:
    def __init__(self):
        self.hh = "hello"
        print("hhhhhh")

tt = TestDemo()
for i in tt:
    print(i)