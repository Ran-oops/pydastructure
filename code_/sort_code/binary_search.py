#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
递归实现:
最优时间复杂度是O(1)
最坏时间复杂度是O(logn)
"""
def binary_search(alist, item):
    """二分查找"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)

    return False


if __name__ == "__main__":
    li = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print(binary_search(li, 55))
