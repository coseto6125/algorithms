# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-20 23:51:47
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 00:22:02
# @url: https://leetcode.com/problems/happy-number/description/
from functools import cache

class Solution:
    def isHappy(self, n: int) -> bool:
        @cache
        def happy(v):
            return sum(int(i)**2 for i in str(v))
        while n>4:
            n = happy(n)
        return n == 1
    
Solution().isHappy(198)