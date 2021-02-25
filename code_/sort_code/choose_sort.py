# coding: utf-8

"""
遍历找到最小的一个元素放在第1个位置
第二小的元素放在第2个位置
"""


def choose_sort(alist):
    n = len(alist)
    # min = 0
    for j in range(n-1):
        minu = j
        for i in range(j+1, n):
            if alist[i] < alist[minu]:
                minu = i
        alist[minu], alist[j] = alist[j], alist[minu]
    print(alist)


if __name__ == "__main__":
    choose_sort([6, 5, 4, 3, 2, 1])
