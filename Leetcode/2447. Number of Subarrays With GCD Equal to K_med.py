# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-20 00:44:05
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-20 03:30:49
# @url: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/submissions/
from math import gcd
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n,res = len(nums), 0
        a = []
        i0 = -1
        for i, x in enumerate(nums):
            if x%k:
                a,i0 = [],i
                continue
            a.append([x,i])
            j = 0
            for p in a:
                p[0] = gcd(p[0],x)
                if a[j][0] != p[0]:
                    j+=1
                    a[j] = p
                else:
                    a[j][1] = p[1]
            del a[j+1:]
            if a[0][0] == k:
                res += a[0][1]-i0
        return res
