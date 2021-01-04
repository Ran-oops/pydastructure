#!/usr/bin/python
# -*- coding: utf-8 -*-

class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1, self.address: "192.168.1.1"}

    def __getitem__(self, key):
        return "hello"


data = DataTest(1, "127.0.0.1")
print(data[2])

# 说明：如果在类中定义了__getitem__()方法，那么他的实例对象假设为p就可以p[key]取值，当实例对象做p[key]
# 运算时， 就会调用__getitem__()方法
