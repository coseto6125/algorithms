# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 23:40:12
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-12-04 03:47:02
# @url: https://leetcode.com/problems/rotate-array/description/
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:]+nums[:-k]