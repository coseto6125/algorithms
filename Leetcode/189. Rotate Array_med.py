# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 23:40:12
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 23:40:37
# @url: https://leetcode.com/problems/rotate-array/description/
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]