# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-23 00:57:45
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:49:03
# @url: https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/


from itertools import accumulate
from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        return next(t for t,i in zip(range(len(chalk)),accumulate(chalk)) if i>k)

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        i = 0
        while k > 0: 
            k -= chalk[i]
            i += 1
        return i - int(k < 0)


Solution().chalkReplacer([98,77,86,89,17,17,89,41,9,27,32,94,24,85,61,17,7,5,66,4,86,89,36,19,68,31,6,92,97,80,70,11,57,4,10,14,49,86,74,1,91,59]

,210951596)