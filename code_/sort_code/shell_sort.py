#!/usr/bin/env python
# -*- coding: utf-8 -*-

def shell_sort(alist):
    """
    希尔排序
    """
    n = len(alist)
    gap = n // 2
    """
    alist = [6, 5, 4, 3, 2, 1, 7, 9, 0]
    n = 9
    gap = 4
    6       2        0
      5       1    
        4       7  
          3       9
            
    (4, 10)
    i=4 5 6 7 8
    """

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap

        gap = gap // 2


if __name__ == "__main__":
    alist = [6, 5, 4, 3, 2, 1, 7, 9, 0]
    shell_sort(alist)
    print(alist)