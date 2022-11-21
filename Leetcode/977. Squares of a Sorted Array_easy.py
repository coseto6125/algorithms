# -*- coding: utf-8 -*-
# @Author: E-NoR
# @Date:   2022-11-21 23:07:09
# @Last Modified by:   E-NoR
# @Last Modified time: 2022-11-21 23:07:39
# @url: https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i*i for i in nums)