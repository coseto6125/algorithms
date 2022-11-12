# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-10-14 23:38:31
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-12 13:44:11
#!/bin/python3
from operator import mul
from random import randint
from clock2 import timeit_choice

class KOS:
    def __init__(self, size):
        self.size = size
        self.arr = [0 for _ in range(self.size)]
    
    def add(self, x, val):
        if x == 0:
            self.arr[0] += val
            return
        while x < self.size:
            self.arr[x] += val
            x += x & (-x)
    
    def level(self, x):
        if x < 0:
            return 0
        res = self.arr[0]
        while x > 0:
            res += self.arr[x]
            x &= x - 1
        return res


@timeit_choice
def sortedSum1(a):
    """
    copy from others
    """
    limit = 10**6
    cap = 10**9 + 7
    pre_a = KOS(limit + 1)
    post_b = KOS(limit + 1)
    cur = res = total = 0
    for i in range(len(a)):
        pos = pre_a.level(a[i]) + 1
        greater = total - post_b.level(a[i])
        cur = (cur + pos * a[i] + greater) % cap
        res = (res + cur) % cap
        pre_a.add(a[i], 1)
        post_b.add(a[i], a[i])
        total += a[i]
    return res

@timeit_choice
def sortedSum2(a):
    """
    base with mul faster when len<1780
    don't tyr enumerate, spend too much time
    """
    M = 10**9 + 7
    p = len(a)+1
    res = 0
    for i in range(1,p):
        res += sum(map(mul,sorted(a[:i]),range(1,i+1)))
    return res%M

@timeit_choice
def sortedSum(a):
    """
    chosee bestway
    """
    if len(a)<1780:
        return sortedSum2(a)
    return sortedSum1(a)

if __name__ == '__main__':
    a_count = 14
    # a = [9,5,8]
    for xr in range(1620,randint(1,10**5)):
        a = [randint(1,10**6) for _ in range(xr)]
    # a = [747402,380408,605449,846906,385224,31431,677517,770001,389085,40373,487560,886252,596334,59083]

    result = sortedSum1(a)
    result = sortedSum2(a)
