# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-10-28 20:20:28
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-23 23:37:51
# @url: https://leetcode.com/problems/number-of-unequal-triplets-in-array
from collections import Counter
from typing import List
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        left, right = 0, len(nums)
        ans = 0
        for mid in Counter(nums).values():
            right -= mid
            ans += left * mid * right
            left += mid
        return ans
Solution().unequalTriplets([4,4,2,4,3]
)