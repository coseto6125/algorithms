# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 00:25:53
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 00:38:32
from functools import cache
from itertools import combinations, cycle
from typing import List
class Solution:
    def check(self,ls):
        @cache
        def step1(a,b,c):
            return all(((a+b) > c, (a+c) > b, (b+c) > a)) 
        return 1 if step1(*ls) else 0
    def triangleNumber(self, nums: List[int]) -> int:
        m = set(combinations(nums,3))
        print(m)
        return sum(map(self.check,set(combinations(nums,3))))
Solution().triangleNumber([2,2,3,4]
)