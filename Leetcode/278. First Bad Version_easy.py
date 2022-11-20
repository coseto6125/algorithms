# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-20 23:39:16
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-20 23:44:28
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo,hi = 1,n+1
        while lo<hi:
            t = lo+((hi-lo)>>1)
            if not isBadVersion(t):
                lo = t+1
            else:
                hi = t
        return hi