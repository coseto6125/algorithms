# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-22 22:43:20
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-22 22:55:17
# @url: https://leetcode.com/problems/move-zeroes/description/
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)
Solution().moveZeroes([0,1,0,3,12]
)