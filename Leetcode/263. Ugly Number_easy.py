# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-19 00:18:46
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-20 23:37:41
# @url: https://leetcode.com/problems/ugly-number/description/
class Solution:

    def isUgly(self, n: int) -> bool:
        if n < 1: return False

        for i in (5, 3, 2):
            while not (n % i):
                n /= i
        return n == 1