# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-20 23:33:52
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:49:28
# @url: https://leetcode.com/problems/binary-search/description/

from typing import List
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        o = bisect_left(nums,target)
        return o if o<len(nums) and nums[o] == target else -1