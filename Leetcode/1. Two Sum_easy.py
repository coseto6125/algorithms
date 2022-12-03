# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 22:17:17
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:46:53
# @url: https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for c, i in enumerate(nums):
            m = target-i
            if num_map.__contains__(m):
                return [num_map[m],c]
            num_map[i] = c