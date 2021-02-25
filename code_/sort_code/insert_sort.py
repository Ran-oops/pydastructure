# coding: utf-8

"""
* 元素列表的第一个数据看作是已排序序列, 其它元素当成未排序序列
* 将之前比自己大的都往后移一位 当前位用key来存着
* 用第一层的循环来知道现在是在插入第几个元素
"""

# def insert_sort(alist):
#     n = len(alist)
#     for i in range(1, n):
#         key = alist[i]
#         j = i-1
#         while j >= 0 and key < alist[j]:
#             alist[j+1] = alist[j]
#             j -= 1
#         alist[j+1] = key
#     print(alist)


def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        j = i
        key = alist[i]
        while j > 0 and key < alist[j - 1]:
            alist[j] = alist[j - 1]
            j -= 1
        alist[j] = key
    print(alist)


if __name__ == "__main__":
    insert_sort([6, 5, 4, 3, 2, 1])
