# coding: utf-8

"""
使用分治法策略来把一个序列分为较小和较大的两个子序列,然后递归地排序两个子序列
* 挑选基准值: 从数列中挑出一个元素,作为"基准"(pivod)
* 分割: 重新排序数列,所有比基准值小的元素放在基准前面,其他放在基准之后
* 递归排序子序列
"""



def quick_sort(alist, first, last):
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时, low==high
    alist[low] = mid_value
    # 对low的列表执行快速排序
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)
    # print(alist)


if __name__ == "__main__":
    li = [6, 5, 4, 3, 2, 1]
    n = len(li)-1
    quick_sort(li, 0, n)
    print(li)
