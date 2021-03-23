# coding: utf-8

"""
时间复杂度
 * 最优时间复杂度:O(n) 表示遍历一次没有发现任何可以交换的元素,排序结束
 * 最坏时间复杂度: O(n²)
 * 稳定性: 稳定

 一个班长 比较两个 找到最大的放在最后
"""

# def bubble_sort(alist):
#     n = len(alist)
#     for j in range(n-1):
#         for i in range(0, n-1-j):
#             if alist[i] > alist[i+1]:
#                 alist[i], alist[i+1] = alist[i+1], alist[i]
#
#     print(alist)


"""
改进方案
"""


def bubble_sort(alist):
    n = len(alist)
    count = 0
    for j in range(n - 1):
        # for i in range(0, n - 1 - j):
        for i in range(n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if count == 0:
            print(alist)
            return
    print(alist)


if __name__ == "__main__":
    bubble_sort([6, 5, 4, 3, 2, 1])
