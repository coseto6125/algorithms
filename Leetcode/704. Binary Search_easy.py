# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-20 23:33:52
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-20 23:35:02
# @url: https://leetcode.com/problems/binary-search/description/

from typing import List
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        o = bisect_left(nums,target)
        if o<len(nums) and nums[o] == target:
            return o
        return -1