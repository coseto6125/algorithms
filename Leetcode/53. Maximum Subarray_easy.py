# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 01:45:49
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:49:18
# @url: https://leetcode.com/problems/maximum-subarray/description/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total,x = nums[0],0
        for i in nums:
            x += i
            if x > total: total = x
            x = max(x, 0)
        return total