# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 01:45:49
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 01:46:27
# @url: https://leetcode.com/problems/maximum-subarray/description/
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total,x = nums[0],0
        for i in nums:
            x += i
            if x > total: total = x
            if x < 0: x = 0
        return total