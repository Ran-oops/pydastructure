# coding: utf-8

from collections.abc import *
c = list()
a=[1,2,3,4]
print(isinstance(a,Iterable))                    # True
print(isinstance(a,Iterator))                    # False

print("################")

print(isinstance(iter(a),Iterable))                    # True
print(isinstance(iter(a),Iterator))                    # True